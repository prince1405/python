#step4

import random

stages = ['''

  +------+
  |      |
  o      |
 /|\     |
 / \     |
         |
============
''', '''
  +------+
  |      |
  o      |
 /|\     |
 /       |
         |
============
''', '''
  +------+
  |      |
  o      |
 /|      |
 /       |
         |
============
''', '''
  +------+
  |      |
  o      |
 /|      |
         |
         |
============
''', '''
  +------+
  |      |
  o      |
  |      |
         |
         |
============
''', '''
  +------+
  |      |
  o      |
         |
         |
         |
============
''', '''
  +------+
  |      |
         |
         |
         |
         |
============
''']

end_of_game = False
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#TODO1 - Create a variable called 'lives' to keep track of the number of lives left.
# Set 'lives' to equal 7.
lives = 7

#Testing code
print(f"Pssst, the solution is {chosen_word}.")

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter:").lower()

  #check guessed letter
    for position in range(word_length):
      letter = chosen_word[position]
      print(f"Current position: {position}\nCurrent letter: {letter}\n Guessed letter: {guess}")
      if letter == guess:
        display[position] = letter
   # else:
      #print("No Match")
#TODO2- If guess is not a letter in the chosen_word,
#Then reduce 'lives' by 1.
#If lives goes down to 0 then the game should stop and it should print "You Lose."
if guess not in chosen_word:
  lives -= 1
  if lives == 0:
    end_of_game = True
    print("You Lose.")
#Join all the elements in the list amnd turn it into a string.
print(f"{' '.join(display)}")

#Check if user has got all letters.
if "_" not in display:
  end_of_game = True
  print("You Win.")
  
#TODO3 - Print the ASCII art from 'stages' that corresponds to the current number of the 'lives' the user has remaining.
print(stages[lives])