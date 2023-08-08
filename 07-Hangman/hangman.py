import random

import hangman_art
from hangman_words import word_list

chosen_word = random.choice(word_list)
lives = 6

print(hangman_art.logo)

display = []
for letter in chosen_word:
    display.append("_")

end_game = "_" not in display

print(f'\nThe secret word is: {" ".join(display)}')

guessed_letters = []
while not end_game:
    while True:
        guess = input("Guess a letter from the word: ").lower()
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        elif len(guess) == 1:
            guessed_letters.append(guess)
            break
        print("Please input a single letter.")
        continue

    for index, letter in enumerate(chosen_word):
        if letter == guess:
            display[index] = letter

    display_string = " ".join(display)

    print(hangman_art.stages[lives])
    print(display_string)
    if guess not in chosen_word:
        print(f"The letter {guess} is not in the secret word. The man is one step closer to be hung!")
        lives -= 1
        if lives == 0:
            print(hangman_art.stages[lives])
            print(f"You lost the game! The secret word was {chosen_word}.")
            end_game = True

    if "_" not in display:
        print("A winner is you!")
        end_game = True
