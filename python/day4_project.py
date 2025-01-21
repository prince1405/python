import random

rock = '''

       ______________
_ _ _ _'   __________)                      
              (_________)
              (__________)
_______       (_________)
       '______(______)

'''
scissors = '''

       -----------
------'    _______)________
               ____________)__
           ___________________)
______     (__________)
      '_____(_______)
'''
paper = '''
       ______________
______'      (_______)
            '________________
             ________________)
             __________________)
             _______________)
-------,________________)

'''
game_images = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
else:
    print(game_images[user_choice])
    0
    computer_choice = random.randint(0, 2)
    print(f"computer choose{computer_choice}")
    print(game_images[computer_choice])
    if user_choice == 0 and computer_choice == 2:
        print("You Win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose!")
    elif computer_choice > user_choice:
        print("You Lose!")
    elif user_choice > computer_choice:
        print("You win!")
    elif computer_choice == user_choice:
        print("It's a draw!")
    else:
        print("You typed an invalid number, you lose!")

