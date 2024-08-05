def encrypt():
    text = input("Enter a message to encrypt: ")
    key = int(input("Enter the key: "))

    encrypted_text = ""
    for ch in text:
        if ch.isalnum():
            if ch.islower():
                encrypted_text += chr((ord(ch) - ord('a') + key) % 26 + ord('a'))
            elif ch.isupper():
                encrypted_text += chr((ord(ch) - ord('A') + key) % 26 + ord('A'))
            elif ch.isdigit():
                encrypted_text += chr((ord(ch) - ord('0') + key) % 10 + ord('0'))
        else:
            print("Invalid Message")
            return

    print("Encrypted message:", encrypted_text)

def decrypt():
    text = input("\nEnter a message to decrypt: ")
    key = int(input("Enter the key: "))

    decrypted_text = ""
    for ch in text:
        if ch.isalnum():
            if ch.islower():
                decrypted_text += chr((ord(ch) - ord('a') - key + 26) % 26 + ord('a'))
            elif ch.isupper():
                decrypted_text += chr((ord(ch) - ord('A') - key + 26) % 26 + ord('A'))
            elif ch.isdigit():
                decrypted_text += chr((ord(ch) - ord('0') - key + 10) % 10 + ord('0'))
        else:
            print("Invalid Message")
            return

    print("Decrypted message:", decrypted_text)

def main():
    encrypt()
    decrypt()

if __name__ == "__main__":
    main()
