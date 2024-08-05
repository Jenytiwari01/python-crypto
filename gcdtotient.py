def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def phi(n):
    result = 1
    for i in range(2, n):
        if gcd(i, n) == 1:
            result += 1
    return result

def main():
    n = int(input("Enter the number: "))
    print(f"phi({n}) = {phi(n)}")

if __name__ == "__main__":
    main()
