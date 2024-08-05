def upper_case(src):
    return src.upper()

def encipher(src, key, is_encode):
    src = upper_case(src)
    key = upper_case(key)

    # Strip out non-letters
    dest = ''.join(c for c in src if c.isalpha())

    klen = len(key)
    result = ''
    for i, char in enumerate(dest):
        if not char.isalpha():
            result += char
            continue
        shift = ord(key[i % klen]) - ord('A')
        if is_encode:
            result += chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
        else:
            result += chr(((ord(char) - ord('A') - shift + 26) % 26) + ord('A'))
    return result

def main():
    str = "Utsav is the student of BSCCSIT"
    key = "VIGENERECIPHER"

    print("Text:", str)
    print("Key:", key)

    cod = encipher(str, key, True)
    print("Cipher Text:", cod)

    dec = encipher(cod, key, False)
    print("Plain Text:", dec)

if __name__ == "__main__":
    main()
