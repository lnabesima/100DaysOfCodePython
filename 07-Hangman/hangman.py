import random

# Step 2

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

display = []
for letter in chosen_word:
    display.append("_")

print(display)

while True:
    guess = input("Guess a letter from the word: ").lower()
    if len(guess) == 1:
        break
    print("Please input a single letter.")
    continue

for index, letter in enumerate(chosen_word):
    if letter == guess:
        display[index] = letter

print(display)
