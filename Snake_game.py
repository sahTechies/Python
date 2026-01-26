import random
import time
import sys
import os
from collections import deque

# Windows-compatible keyboard input
if os.name == 'nt':
    import msvcrt

    def get_key():
        """Get a single key; supports arrows and WASD on Windows."""
        if not msvcrt.kbhit():
            return None

        key = msvcrt.getch()
        # Arrow keys come as a prefix byte then a code byte
        if key in (b"\x00", b"\xe0"):
            special = msvcrt.getch()
            mapping = {
                b"H": "up",    # Arrow up
                b"P": "down",  # Arrow down
                b"K": "left",  # Arrow left
                b"M": "right", # Arrow right
            }
            return mapping.get(special)

        try:
            return key.decode().lower()
        except UnicodeDecodeError:
            return None
else:
    import select

    def get_key():
        """Get a single key; supports arrows and WASD on POSIX terminals."""
        if not select.select([sys.stdin], [], [], 0)[0]:
            return None

        first = sys.stdin.read(1)
        if first != "\x1b":
            return first.lower()

        # Attempt to parse escape sequence for arrows
        if select.select([sys.stdin], [], [], 0)[0]:
            rest = sys.stdin.read(2)
            mapping = {
                "[A": "up",
                "[B": "down",
                "[D": "left",
                "[C": "right",
            }
            return mapping.get(rest)
        return None

# Constants
GRID_WIDTH = 40
GRID_HEIGHT = 20

# Game symbols
SNAKE_HEAD = "●"
SNAKE_BODY = "○"
FOOD = "◆"
BONUS = "★"
EMPTY = " "
BORDER = "█"

class Direction:
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

class SnakeGame:
    def __init__(self):
        self.reset_game()
    
    def reset_game(self):
        """Initialize or reset game state"""
        self.snake = deque([(GRID_WIDTH // 2, GRID_HEIGHT // 2)])
        self.direction = Direction.RIGHT
        self.next_direction = Direction.RIGHT
        self.food = self.spawn_food()
        self.bonus = None
        self.bonus_timer = 0
        self.next_bonus_score = 50
        self.score = 0
        self.game_over = False
    
    def spawn_food(self):
        """Spawn food at a random location not occupied by snake"""
        while True:
            x = random.randint(1, GRID_WIDTH - 2)
            y = random.randint(1, GRID_HEIGHT - 2)
            if (x, y) not in self.snake:
                return (x, y)

    def spawn_bonus(self):
        """Spawn bonus at a random free cell"""
        while True:
            x = random.randint(1, GRID_WIDTH - 2)
            y = random.randint(1, GRID_HEIGHT - 2)
            if (x, y) not in self.snake and (x, y) != self.food:
                return (x, y)
    
    def update(self):
        """Update game state"""
        if self.game_over:
            return
        
        self.direction = self.next_direction
        
        # Calculate new head position
        head_x, head_y = self.snake[0]
        dx, dy = self.direction
        new_head = (head_x + dx, head_y + dy)
        
        # Check wall collision
        if (new_head[0] <= 0 or new_head[0] >= GRID_WIDTH - 1 or
            new_head[1] <= 0 or new_head[1] >= GRID_HEIGHT - 1):
            self.game_over = True
            return
        
        # Check self collision
        if new_head in self.snake:
            self.game_over = True
            return
        
        # Add new head
        self.snake.appendleft(new_head)
        
        # Check food collision
        if new_head == self.food:
            self.score += 10
            self.food = self.spawn_food()
            # Trigger bonus spawn every 50 points
            if self.score >= self.next_bonus_score and self.bonus is None:
                self.bonus = self.spawn_bonus()
                self.bonus_timer = 0
        else:
            # Remove tail if no food eaten
            self.snake.pop()

        # Check bonus collision
        if self.bonus and new_head == self.bonus:
            self.score += 100
            self.bonus = None
            self.next_bonus_score += 50

        # Bonus lifetime handling
        if self.bonus:
            self.bonus_timer += 1
            if self.bonus_timer >= 120:  # roughly 12 seconds at 10 FPS
                self.bonus = None
                self.next_bonus_score += 50
    
    def draw(self):
        """Draw game elements to terminal"""
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # Draw top border
        print("╔" + "═" * (GRID_WIDTH - 2) + "╗")
        
        # Draw grid
        for y in range(1, GRID_HEIGHT - 1):
            row = "║"
            for x in range(1, GRID_WIDTH - 1):
                if (x, y) == self.food:
                    row += FOOD
                elif self.bonus and (x, y) == self.bonus:
                    row += BONUS
                elif (x, y) == self.snake[0]:
                    row += SNAKE_HEAD
                elif (x, y) in self.snake:
                    row += SNAKE_BODY
                else:
                    row += EMPTY
            row += "║"
            print(row)
        
        # Draw bottom border
        print("╚" + "═" * (GRID_WIDTH - 2) + "╝")
        
        # Draw score
        print(f"\nScore: {self.score}")
        
        if self.game_over:
            print("\n╔════════════════════╗")
            print("║   GAME OVER! 💀    ║")
            print("╚════════════════════╝")
            print("\nPress 'r' to restart or 'q' to quit")
    
    def run(self):
        """Main game loop"""
        print("🐍 SNAKE GAME 🐍")
        print("\nControls: w=up, s=down, a=left, d=right, q=quit")
        print("Press any key to start (q to quit)...\n")
        # Wait for any key to begin; allow quitting with 'q'
        while True:
            key = get_key()
            if key:
                if key == 'q':
                    return
                break
            time.sleep(0.05)
        
        while True:  # Outer loop for restarting
            move_counter = 0
            
            try:
                while not self.game_over:
                    self.draw()
                    
                    # Simple timing for movement
                    move_counter += 1
                    if move_counter >= 2:
                        self.update()
                        move_counter = 0
                    
                    # Get keyboard input
                    key = get_key()
                    if key:
                        if key in ('w', 'up') and self.direction != Direction.DOWN:
                            self.next_direction = Direction.UP
                        elif key in ('s', 'down') and self.direction != Direction.UP:
                            self.next_direction = Direction.DOWN
                        elif key in ('a', 'left') and self.direction != Direction.RIGHT:
                            self.next_direction = Direction.LEFT
                        elif key in ('d', 'right') and self.direction != Direction.LEFT:
                            self.next_direction = Direction.RIGHT
                        elif key == 'q':
                            return  # Exit the game
                    
                    time.sleep(0.1)
                
                # Final draw for game over
                self.draw()
                
                # Restart prompt
                while True:
                    restart_key = get_key()
                    if restart_key:
                        if restart_key == 'r':
                            self.reset_game()
                            break
                        elif restart_key == 'q':
                            return  # Exit the game
                    time.sleep(0.1)
                
            except KeyboardInterrupt:
                print("\n\nGame interrupted. Thanks for playing!")
                return

if __name__ == "__main__":
    game = SnakeGame()
    game.run()