def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if the character is an alphabet
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char  # Non-alphabet characters are unchanged
    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift)  # Decrypting is just encrypting with the negative shift

def main():
    while True:
        choice = input("Do you want to (e)ncrypt or (d)ecrypt? (q to quit): ").lower()
        if choice == 'q':
            break
        if choice not in ('e', 'd'):
            print("Invalid choice. Please choose 'e' to encrypt or 'd' to decrypt.")
            continue
        
        message = input("Enter the message: ")
        shift = int(input("Enter the shift value (1-25): "))
        
        if choice == 'e':
            encrypted_message = encrypt(message, shift)
            print(f"Encrypted message: {encrypted_message}")
        elif choice == 'd':
            decrypted_message = decrypt(message, shift)
            print(f"Decrypted message: {decrypted_message}")

if __name__ == "__main__":
    main()