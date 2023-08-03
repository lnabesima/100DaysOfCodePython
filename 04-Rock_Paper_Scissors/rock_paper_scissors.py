import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇

options = [rock, paper, scissors]
options_names = ["Rock", "Paper", "Scissors"]
print("Welcome to an exciting game of Rock, Paper, Scissors!")
print("The rules are simple: Rock beats Scissors, Scissors beats Paper, Paper beats Rock.\n")

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice in range(3):
    print(f'You\'ve chosen {options_names[user_choice]}!')
    print(options[user_choice])

computer_choice = random.randint(0, 2)
print(f"The computer chooses {options_names[computer_choice]}!")
print(options[computer_choice])

if user_choice == computer_choice:
    print("It's a draw!")
    exit()

options_names = ["Rock", "Paper", "Scissors"]

if user_choice == 0:
    if computer_choice == 1:
        print(f'{options_names[computer_choice]} beats {options_names[user_choice]}. You lose!')
    else:
        print(f'{options_names[user_choice]} beats {options_names[computer_choice]}. You win!')
elif user_choice == 1:
    if computer_choice == 0:
        print(f'{options_names[user_choice]} beats {options_names[computer_choice]}. You win!')
    else:
        print(f'{options_names[computer_choice]} beats {options_names[user_choice]}. You lose!')
else:
    if computer_choice == 0:
        print(f'{options_names[user_choice]} beats {options_names[computer_choice]}. You win!')
    else:
        print(f'{options_names[computer_choice]} beats {options_names[user_choice]}. You lose!')
