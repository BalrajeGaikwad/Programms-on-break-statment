import random

choicess=["rock","paper","scissors"]
player_card=0
computer_score=0

while True:
    player_choice=random.choice(choicess)
    computer_choice=random.choice(choicess)
    print(f"player :{player_choice}, computer: {computer_choice}")



    if player_choice==computer_choice:
        print("its a tie !")
    elif (player_choice== "rock" and computer_choice =="scissors") or \
          (player_choice== "scissors" and computer_choice =="paper") or \
          (player_choice== "paper" and computer_choice =="rock"):
        print("Player win the match")
        player_card+=1

    else:
        print("computer win the match ")
        computer_score+=1

    if player_card == 3 or computer_score == 3:
        print(f"Game over! Final Score - Player: {player_card}, Computer: {computer_score}")
        break