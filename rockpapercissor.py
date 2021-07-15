import random
import time

coups = ["Rock", "Paper", "Scissor"]

print("-"*50)
print("Welcome to the Rock Paper Scissor game !")
print("Rules : the paper beat the rock, the scissor beat the paper and the rock beat the scissor !")
print("Lets Play !")

while True:
    ia_choice = random.choice(coups)
    print("-"*50)
    print("Type your choice (Rock, Paper or Scissor) !")
    player_choice = input("Enter your choice :")
    print("1...")
    time.sleep(0.75)
    print("2...")
    time.sleep(0.75)
    print("3 !")
    time.sleep(0.75)
    
    if player_choice == str(ia_choice):
        print(f"You choose {player_choice}, the IA choose {ia_choice} : you draw !")
    elif player_choice == coups[0] and ia_choice == coups[2]:
        print("You choose Rock, IA choose Scissor : you win !") 
    elif player_choice == coups[0] and ia_choice == coups[1]:
        print("You choose Rock, IA choose Paper : you lose !")
    elif player_choice == coups[1] and ia_choice == coups[2]:
        print("You choose Paper, IA choose Scissor : you lose !")
    elif player_choice == coups[1] and ia_choice == coups[0]:
        print("You choose Paper, IA choose Rock : you win !")
    elif player_choice == coups[2] and ia_choice == coups[0]:
        print("You choose Scissor, IA choose Rock : you lose !")
    elif player_choice == coups[2] and ia_choice == coups[1]:
        print("You choose Scissor, IA choose Paper : you win !")        