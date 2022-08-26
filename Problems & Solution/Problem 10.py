#
# Problem 10. Summation of primes
# Link : https://projecteuler.net/problem=10
#
import math

def Cal(num):
    # Use Sieve of Eratosthenes
    max_num = int(math.sqrt(num)) + 1
    for i in range(2, max_num):
        if num % i == 0:
            return False
    return True

if __name__ == "__main__":
    print(sum(list(filter(Cal, range(2, 2000000)))))