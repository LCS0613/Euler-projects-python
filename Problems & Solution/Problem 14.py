#
# Problem 14. Longest Collatz sequence
# Link : https://projecteuler.net/problem=14
#

# Define discriminant function for even/odd numbers
def is_odd(num):
    if num % 2 != 0:
        return True
    else:
        return False

def Cal():
    count = 0
    result = 0

    for i in range(1, 1000001):
        count_temp = 0
        result_temp = i

        while i != 1:
            if is_odd(i):
                i = 3 * i + 1
                count_temp += 1
            else:
                i = i / 2
                count_temp += 1

        if count_temp > count:
            count = count_temp
            result = result_temp

    return result

if __name__ == "__main__":
    print(Cal())