import math


def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


def main():
    """Main logic to print prime numbers less than 100."""
    for i in range(100):
        if is_prime(i):
            print(i, end=' ')
    print()


if __name__ == '__main__':
    main()
