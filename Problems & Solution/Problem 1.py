#
# Problem 1. Multiples of 3 or 5
# Link : https://projecteuler.net/problem=1
#

# Define 'Cal' function to calculate result value
def Cal():
    result = 0
    for i in range(1, 1000):
        if i % 3 == 0 or i % 5 == 0:
            result += i
    return result

if __name__ == "__main__":
    print(Cal())