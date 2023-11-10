#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------
# write 'hello world' to the console
print("Hello, World!")
from flask import Flask
app = Flask(__name__)

# import random module
import random
def play_minigame():
    # initialize mini-game rock-paper-scissors score
    score = {'player': 0, 'computer': 0, 'tie': 0}
    while True:
        # Ask for the player's choice
        print("Choose: rock, paper, or scissors")
        player_choice = input().lower()
        # Validate player input
        if player_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid option. Please choose rock, paper, or scissors.")
            continue
        # Random choice for the computer
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        print(f"The computer chose: {computer_choice}")
        # Determine the winner of the round
        result = determine_winner(player_choice, computer_choice)
        # Update the score and display the result
        update_score(result, score)
        display_result(result)
        # Ask if the player wants to play again
        play_again = input("Want to play again? (y/n)").lower()
        if play_again != 'y':
            end_minigame(score)
            break

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return 'tie'
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'scissors' and computer_choice == 'paper') or \
         (player_choice == 'paper' and computer_choice == 'rock'):
        return 'player'
    else:
        return 'computer'

def update_score(result, score):
    if result == 'tie':
        score['tie'] += 1
    elif result == 'player':
        score['player'] += 1
    else:
        score['computer'] += 1

def display_result(result):
    if result == 'tie':
        print("It's a tie!")
    elif result == 'player':
        print("You won!")
    else:
        print("You lost!")

def end_minigame(score):
    print("Game over. Final score:")
    print(f"Player wins: {score['player']}")
    print(f"Total rounds played: {sum(score.values())}")

if __name__ == "__main__":
    play_minigame()

@app.route("/")
def hello():
    return app.send_static_file("index.html")
