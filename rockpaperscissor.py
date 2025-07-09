
import random

user_score = 0
comp_score = 0

while True:
    user_selection = input("Choose rock, paper, or scissor (or type 'quit' to exit): ").lower()
    if user_selection == 'quit':
        print(f"\n🏁 Final Score - You: {user_score}, Computer: {comp_score}")
        break

    choices = ["rock", "paper", "scissor"]
    if user_selection not in choices:
        print("❌ Invalid choice. Try again.\n")
        continue

    comp_choice = random.choice(choices)
    print(f"🤖 Computer chose: {comp_choice}")

    if user_selection == comp_choice:
        print("⚖ It's a tie!\n")
    elif (user_selection == "rock" and comp_choice == "scissor") or \
        (user_selection == "paper" and comp_choice == "rock") or \
        (user_selection == "scissor" and comp_choice == "paper"):
        print("✅ You won!\n")
        user_score += 1
    else:
        print("❌ You lose!\n")
        comp_score += 1

    print(f"🔢 Score - You: {user_score}, Computer: {comp_score}\n")
