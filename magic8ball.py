import random

# Classic Magic 8-Ball responses (10 yes, 5 maybe, 5 no)
responses = [
    "It is certain.", "It is decidedly so.", "Without a doubt.",
    "Yes – definitely.", "You may rely on it.", "As I see it, yes.",
    "Most likely.", "Outlook good.", "Signs point to yes.", "Yes.",
    "Reply hazy, try again.", "Ask again later.", "Better not tell you now.",
    "Cannot predict now.", "Concentrate and ask again.",
    "Don't count on it.", "My reply is no.", "My sources say no.",
    "Outlook not so good.", "Very doubtful."
]

def magic_8_ball():
    print("🎱 Welcome to Magic 8-Ball! 🎱")
    print("Ask a yes/no question (or 'quit' to exit)\n")
    
    while True:
        question = input("Your question: ").strip()
        
        if question.lower() == 'quit':
            print("👋 Thanks for playing!")
            break
            
        if not question:
            print("Please ask a real question!\n")
            continue
            
        print("🔮 Shaking...")
        import time
        time.sleep(1.5)
        
        answer = random.choice(responses)
        print(f"🎱 Magic 8-Ball says: {answer}\n")

# Run the game
magic_8_ball()
