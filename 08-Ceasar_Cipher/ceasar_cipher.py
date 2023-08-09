alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
alphabet_length = len(alphabet)


def caesar_cipher(text_to_transform, shift_amount, selected_direction):
    new_text = ""
    direction_options = ['encode', 'decode']
    if selected_direction not in direction_options:
        print("Invalid direction. Please enter either 'encode' or 'decode'.")
        return
    if selected_direction == 'decode':
        shift_amount *= -1
    for letter in text_to_transform:
        if letter in alphabet:
            current_letter = alphabet.index(letter)
            shifted_letter = (current_letter + shift_amount) % alphabet_length
            new_text += alphabet[shifted_letter]
        else:
            new_text += letter
    print(new_text)


print(logo)
user_wants_to_continue = True
while user_wants_to_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar_cipher(text_to_transform=text, shift_amount=shift, selected_direction=direction)
    go_again = input("Do you want to go again? Type 'yes' or 'no':\n").lower()
    if go_again == 'no':
        print("Goodbye")
        user_wants_to_continue = False
