import random
import time
import sys
import os
from collections import deque

# Windows-compatible keyboard input
if os.name == 'nt':
    import msvcrt
    def get_key():
        if msvcrt.kbhit():
            return msvcrt.getch().decode().lower()
        return None
else:
    import select
    def get_key():
        if select.select([sys.stdin], [], [], 0)[0]:
            return sys.stdin.read(1).lower()
        return None

# Constants
GRID_WIDTH = 40
GRID_HEIGHT = 20

# Game symbols
SNAKE_HEAD = "●"
SNAKE_BODY = "○"
FOOD = "◆"
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
        self.score = 0
        self.game_over = False
    
    def spawn_food(self):
        """Spawn food at a random location not occupied by snake"""
        while True:
            x = random.randint(1, GRID_WIDTH - 2)
            y = random.randint(1, GRID_HEIGHT - 2)
            if (x, y) not in self.snake:
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
        else:
            # Remove tail if no food eaten
            self.snake.pop()
    
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
            print("\nPress Ctrl+C and run the program again to play another game")
    
    def run(self):
        """Main game loop"""
        print("🐍 SNAKE GAME 🐍")
        print("\nControls: w=up, s=down, a=left, d=right, q=quit")
        print("Press any key to start...\n")
        input()
        
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
                    if key == 'w' and self.direction != Direction.DOWN:
                        self.next_direction = Direction.UP
                    elif key == 's' and self.direction != Direction.UP:
                        self.next_direction = Direction.DOWN
                    elif key == 'a' and self.direction != Direction.RIGHT:
                        self.next_direction = Direction.LEFT
                    elif key == 'd' and self.direction != Direction.LEFT:
                        self.next_direction = Direction.RIGHT
                    elif key == 'q':
                        break
                
                time.sleep(0.1)
            
            # Final draw for game over
            self.draw()
            
        except KeyboardInterrupt:
            print("\n\nGame interrupted. Thanks for playing!")

if __name__ == "__main__":
    game = SnakeGame()
    game.run()