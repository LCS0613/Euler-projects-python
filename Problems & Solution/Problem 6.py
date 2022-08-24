#
# Problem 6. Sum square difference
# Link : https://projecteuler.net/problem=6
#

# Cal1: Calculate sum of the squares
def Cal1():
    result = 0
    for i in range(1,101):
        result += i ** 2
    return result

# Cal2: Caculate square of the sum
def Cal2():
    result = 0
    for i in range(1,101):
        result += i
    return result ** 2

if __name__ == "__main__":
    print(Cal2() - Cal1())
