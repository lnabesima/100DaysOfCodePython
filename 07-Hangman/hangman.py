import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
lives = 6
# Testing code
print(f'Pssst, the solution is {chosen_word}.')

display = []
for letter in chosen_word:
    display.append("_")

end_game = "_" not in display

print(display)
while not end_game:
    while True:
        guess = input("Guess a letter from the word: ").lower()
        if len(guess) == 1:
            break
        print("Please input a single letter.")
        continue

    for index, letter in enumerate(chosen_word):
        if letter == guess:
            display[index] = letter

    display_string = " ".join(display)

    print(stages[lives])
    print(display_string)
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            print(stages[lives])
            print("You lost the game!")
            end_game = True

    if "_" not in display:
        print("You won the game!")
        end_game = True
