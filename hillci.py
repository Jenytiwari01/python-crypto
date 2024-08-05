import numpy as np

encrypt = np.zeros((3, 1))
decrypt = np.zeros((3, 1))
a = np.zeros((3, 3))
b = np.zeros((3, 3))
mes = np.zeros((3, 1))
c = np.zeros((3, 3))

def encryption():
    global encrypt
    for i in range(3):
        for j in range(1):
            for k in range(3):
                encrypt[i][j] += a[i][k] * mes[k][j]
    print("\nEncrypted string is: ", end="")
    for i in range(3):
        print(chr(int(encrypt[i][0] % 26) + 97), end="")

def decryption():
    global decrypt
    inverse()
    for i in range(3):
        for j in range(1):
            for k in range(3):
                decrypt[i][j] += b[i][k] * encrypt[k][j]
    print("\nDecrypted string is: ", end="")
    for i in range(3):
        print(chr(int(decrypt[i][0] % 26) + 97), end="")
    print()

def getKeyMessage():
    global a, c, mes
    print("Enter 3x3 matrix for key (It should be inversible):")
    for i in range(3):
        for j in range(3):
            a[i][j] = float(input())
            c[i][j] = a[i][j]
    msg = input("\nEnter a 3 letter string: ")
    for i in range(3):
        mes[i][0] = ord(msg[i]) - 97

def inverse():
    global b, c
    b = np.identity(3)
    for k in range(3):
        for i in range(3):
            p = c[i][k]
            q = c[k][k]
            for j in range(3):
                if i != k:
                    c[i][j] = c[i][j] * q - p * c[k][j]
                    b[i][j] = b[i][j] * q - p * b[k][j]
    for i in range(3):
        for j in range(3):
            b[i][j] = b[i][j] / c[i][i]
    print("\n\nInverse Matrix is:\n", b)

def main():
    getKeyMessage()
    encryption()
    decryption()

if __name__ == "__main__":
    main()
