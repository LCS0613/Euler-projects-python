#
# Problem 4. Largest palindrome product
# Link : https://projecteuler.net/problem=4
#

# Define 'Cal' function to calculate result value
def Cal():
    result = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            n = i * j
            n_str = str(n)
            if n_str == n_str[::-1] and n > result:
                result = n
    return result

if __name__ == "__main__":
    print(Cal())