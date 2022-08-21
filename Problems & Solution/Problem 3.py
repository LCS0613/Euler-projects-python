#
# Problem 3. Largest prime factor
# Link : https://projecteuler.net/problem=3
#

# Define 'Cal' function to calculate result value
def Cal():
    number = 600851475143
    n = 2

    while n < number:
        if number % n == 0:
            number = number / n
        else:
            n += 1

    return number

if __name__ == '__main__':
    print(Cal())

# You can also get same result using "primefactors" method in SYMPY
# sympy.primefactors(number)