#
# Problem 16. Power digit sum
# Link : https://projecteuler.net/problem=16
#

def Cal():
    n = 2 ** 1000
    n_str = str(n)
    result = 0

    for num in n_str:
        result += int(num)

    return result

if __name__ == "__main__":
    print(Cal())