def gcd(n1, n2):
    if n2 != 0:
        return gcd(n2, n1 % n2)
    else:
        return n1

def main():
    m = int(input("Enter the modulo value:\n"))
    for j in range(m):
        if gcd(j, m) == 1:
            for i in range(1, j + 1):
                s = (i * m) + i
                MI = s % m
                if MI % j == 0:
                    break
            print(f"Multiplicative inverse of {j} is {MI}")
        else:
            print(f"Multiplicative inverse of {j} cannot be calculated")

if __name__ == "__main__":
    main()
