alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
alphabet_length = len(alphabet)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar_cipher(text_to_transform, shift_amount, selected_direction):
    new_text = ""
    direction_options = ['encode', 'decode']
    if selected_direction not in direction_options:
        print("Invalid direction. Please enter either 'encode' or 'decode'.")
        return
    for letter in text_to_transform:
        if letter in alphabet:
            current_letter = alphabet.index(letter)
            shifted_letter = (current_letter + shift_amount) % alphabet_length if selected_direction == 'encode' else \
                current_letter - shift_amount
            new_text += alphabet[shifted_letter]
    print(new_text)


caesar_cipher(text_to_transform=text, shift_amount=shift, selected_direction=direction)
