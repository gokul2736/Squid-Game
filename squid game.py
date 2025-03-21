
import random

def rock_paper_scissors():
    print("🔺 Welcome to Squid Game: Rock-Paper-Scissors! 🔻")
    print("🎭 Hey player 001 Win or die")

    choices = ["rock", "paper", "scissors"]
    player_score = 0
    round_number = 1

    while True:
        print(f"\n🎲 ROUND {round_number}")
        player_choice = input("✋ Enter (rock, paper, scissors) or 'exit': ").strip().lower()

        if player_choice == "exit":
            print("\n📢 FINAL SCORE:")
            print(f"🏆 Player 001: {player_score}")
            print("👋 You survived. For now...")
            break

        if player_choice not in choices:
            print("⚠ Invalid choice! Try again.")
            continue

        computer_choice = random.choice(choices)
        print(f"🤖 The computer chose: {computer_choice}")

        if player_choice == computer_choice:
            print("⚖ It's a tie! You live... for now.")
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "paper" and computer_choice == "rock") or \
             (player_choice == "scissors" and computer_choice == "paper"):
            print("✅ Player 001 wins! The game continues...")
            player_score += 1
        else:
            print("❌ You die.")
            print("💀 GAME OVER.")
            break  # Immediate elimination

        round_number += 1  # Increase round count

rock_paper_scissors()