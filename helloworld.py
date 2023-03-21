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
possible_position = [rock, paper, scissors]
user_input = int(input(" What do you choose? type 0 for Rock, 1 for Paper and 2 for Scissors.\n "))
if user_input >= 3 or user_input < 0:
    print("You typed invalid number, You lose")
else:
    print("User_Choice:")
    user_choice = possible_position[user_input]
    print(user_choice)

    computer_ran_choice = random.randint(0, 2)
    computer_choice = (possible_position[computer_ran_choice])
    print(f" Computer_Choice:\n", computer_choice)

    if user_choice == 0 and computer_choice == 2:
        print("You lose")
    elif computer_choice == 0 and user_choice == 2:
        print("You win")
    elif user_choice > computer_choice:
        print("You win")
    elif computer_choice > user_choice:
        print("Computer win")
    elif user_choice == computer_choice:
        print("It's a draw")
