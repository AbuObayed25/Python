import random

choices = ["Rock", "Paper", "Scissors"]

player1_score = 0
player2_score = 0

while True:
    try:
        player1 = input("Player 1, enter Rock, Paper or Scissors: ").capitalize()
        if player1 not in choices:
            raise ValueError("Invalid input. Please enter Rock, Paper or Scissors.")

        player2 = input("Player 2, enter Rock, Paper or Scissors: ").capitalize()
        if player2 not in choices:
            raise ValueError("Invalid input. Please enter Rock, Paper or Scissors.")

        if player1 == player2:
            print("It's a tie!")
        elif (player1 == "Rock" and player2 == "Scissors") or (player1 == "Scissors" and player2 == "Paper") or (
                player1 == "Paper" and player2 == "Rock"):
            print("Player 1 wins!")
            player1_score += 1
        else:
            print("Player 2 wins!")
            player2_score += 1

        print(f"Score - Player 1: {player1_score}, Player 2: {player2_score}")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

    except ValueError as e:
        print(e)

print("Final Scores:")
print(f"Player 1: {player1_score}")
print(f"Player 2: {player2_score}")
