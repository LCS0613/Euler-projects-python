#
# Problem 12. Highly divisible triangular number
# Link : https://projecteuler.net/problem=12
#

import math

def divisor(num):
    # Use Sieve of Eratosthenes
    count = 0
    max_num = int(math.sqrt(num)) + 1

    for i in range(1, max_num):
        if num % i == 0:
            count += 2
    if (max_num - 1) ** 2 == num:
        count -= 1

    return count

def Cal():
    tri_num = 0
    i = 1
    bool = True

    while bool:
        tri_num = tri_num + i
        if divisor(tri_num) >= 500:
            bool = False
        i = i + 1

    return tri_num

if __name__ == "__main__":
    print(Cal())
