SIZE = 30

# This function will convert the string to lowercase
def toLowerCase(plain):
    return plain.lower()

# This function will remove all the spaces
def removeSpaces(plain):
    return plain.replace(" ", "")

# This function will generate the 5x5 grid square
def generateKeyTable(key):
    keyT = [['' for _ in range(5)] for _ in range(5)]
    key_index = 0
    used_letters = set()

    # Filling the key matrix
    for i in range(5):
        for j in range(5):
            if key_index < len(key):
                while key[key_index] in used_letters or key[key_index] == 'j':
                    key_index += 1
                    if key_index >= len(key):
                        break
                if key_index < len(key):
                    keyT[i][j] = key[key_index]
                    used_letters.add(key[key_index])
                    key_index += 1

    # Filling remaining cells with remaining letters of the alphabet
    for i in range(5):
        for j in range(5):
            if keyT[i][j] == '':
                for letter in 'abcdefghiklmnopqrstuvwxyz':
                    if letter not in used_letters:
                        keyT[i][j] = letter
                        used_letters.add(letter)
                        break
    return keyT

# This function will search for the characters of a digraph in the key and return position of key
def search(keyT, a, b):
    arr = [0] * 4  # Define arr here
    for i in range(5):
        for j in range(5):
            if keyT[i][j] == a:
                arr[0] = i
                arr[1] = j
            elif keyT[i][j] == b:
                arr[2] = i
                arr[3] = j
    return arr  # Return arr

# This function will encrypt plain text using Playfair Cipher algorithm
def encryptByPlayfairCipher(plain, key):
    plain = toLowerCase(plain)
    plain = removeSpaces(plain)
    plain = plain.replace("j", "i")  # Replace 'j' with 'i'
    keyT = generateKeyTable(key)
    ps = len(plain)

    # Making the plain text length even
    if ps % 2 != 0:
        plain += 'z'

    cipher = ""
    for i in range(0, ps, 2):
        arr = search(keyT, plain[i], plain[i + 1])  # Use the search function here
        if arr[0] == arr[2]:  # If characters are in the same row
            cipher += keyT[arr[0]][(arr[1] + 1) % 5]
            cipher += keyT[arr[0]][(arr[3] + 1) % 5]
        elif arr[1] == arr[3]:  # If characters are in the same column
            cipher += keyT[(arr[0] + 1) % 5][arr[1]]
            cipher += keyT[(arr[2] + 1) % 5][arr[1]]
        else:  # If characters form a rectangle/square
            cipher += keyT[arr[0]][arr[3]]
            cipher += keyT[arr[2]][arr[1]]

    return cipher

# This function will decrypt cipher text using Playfair Cipher algorithm
def decryptByPlayfairCipher(cipher, key):
    keyT = generateKeyTable(key)
    ps = len(cipher)
    plain = ""

    for i in range(0, ps, 2):
        arr = search(keyT, cipher[i], cipher[i + 1])  # Use the search function here
        if arr[0] == arr[2]:  # If characters are in the same row
            plain += keyT[arr[0]][(arr[1] - 1) % 5]
            plain += keyT[arr[0]][(arr[3] - 1) % 5]
        elif arr[1] == arr[3]:  # If characters are in the same column
            plain += keyT[(arr[0] - 1) % 5][arr[1]]
            plain += keyT[(arr[2] - 1) % 5][arr[1]]
        else:  # If characters form a rectangle/square
            plain += keyT[arr[0]][arr[3]]
            plain += keyT[arr[2]][arr[1]]

    return plain

# Main code
def main():
    key = "Algorithm"
    print("Key text:", key)

    # Plaintext
    plain = "Jeny"
    print("Plain text:", plain)

    # Encryption using the Playfair Cipher algorithm
    cipher = encryptByPlayfairCipher(plain, key)
    print("Cipher text:", cipher)

    # Decryption using the Playfair Cipher algorithm
    decrypted_plain = decryptByPlayfairCipher(cipher, key)
    print("Deciphered text:", decrypted_plain)

if __name__ == "__main__":
    main()
