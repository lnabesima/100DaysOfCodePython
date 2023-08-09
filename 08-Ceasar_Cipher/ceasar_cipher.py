alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(plain_text, shift_amount):
    alphabet_length = len(alphabet)
    encrypted_text = ""
    for letter in plain_text:
        current_letter = alphabet.index(letter)
        shifted_letter = (current_letter + shift_amount) % alphabet_length
        encrypted_text += alphabet[shifted_letter]
    print(encrypted_text)


if direction == "encode":
    encrypt(text, shift)
