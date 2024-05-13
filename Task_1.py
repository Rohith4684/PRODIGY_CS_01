def caesar_cipher_encrypt(plain_text, shift):
    encrypted_text = ""
    for char in plain_text:
        if char.isalpha():
            shifted_char = chr(
                (ord(char) - ord('a' if char.islower() else 'A') + shift) % 26 + ord('a' if char.islower() else 'A'))
            encrypted_text += shifted_char
        else:
            encrypted_text += char
    return encrypted_text


def caesar_cipher_decrypt(cipher_text, shift):
    decrypted_text = ""
    for char in cipher_text:
        if char.isalpha():
            shifted_char = chr(
                (ord(char) - ord('a' if char.islower() else 'A') - shift) % 26 + ord('a' if char.islower() else 'A'))
            decrypted_text += shifted_char
        else:
            decrypted_text += char
    return decrypted_text


def main():
    while True:
        choice = input("Do you want to encrypt or decrypt? (e/d): ").strip().lower()
        if choice not in ['e', 'd']:
            print("Invalid choice. Please enter 'e' for encryption or 'd' for decryption.")
            continue

        text = input("Enter the text: ")
        shift = int(input("Enter the shift value: "))

        if choice == 'e':
            result = caesar_cipher_encrypt(text, shift)
            print("Encrypted text:", result)
        else:
            result = caesar_cipher_decrypt(text, shift)
            print("Decrypted text:", result)

        another = input("Do you want to perform another operation? (yes/no): ").strip().lower()
        if another != 'yes':
            break


if __name__ == "__main__":
    main()
