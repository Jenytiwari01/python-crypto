import math

# Returns true if n is prime
def isPrime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Iterative Function to calculate (x^n)%p in O(log y)
def power(x, y, p):
    res = 1
    x = x % p

    while y > 0:
        if y & 1:
            res = (res * x) % p
        y = y >> 1
        x = (x * x) % p
    return res

# Utility function to store prime factors of a number
def findPrimefactors(s, size, n):
    i = 2
    while i * i <= n:
        while n % i == 0:
            s.append(i)
            n = n // i
        i += 1
    if n > 1:
        s.append(n)

# Function to find smallest primitive root of n
def findPrimitive(n):
    s = []
    size = 0

    # Check if n is prime or not
    if not isPrime(n):
        return -1

    # Find value of Euler Totient function of n
    phi = n - 1

    # Find prime factors of phi and store in an array
    findPrimefactors(s, size, phi)

    # Check for every number from 2 to phi
    for r in range(2, phi + 1):
        # Iterate through all prime factors of phi.
        # and check if we found a power with value 1
        flag = False
        for i in range(len(s)):
            # Check if r^((phi)/primefactors) mod n
            # is 1 or not
            if power(r, phi // s[i], n) == 1:
                flag = True
                break
        # If there was no power with value 1.
        if not flag:
            return r

    # If no primitive root found
    return -1

def main():
    n = int(input("Enter the number: "))
    print(f"Smallest primitive root of {n} is {findPrimitive(n)}")

if __name__ == "__main__":
    main()
