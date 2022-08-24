#
# Problem 7. 10001st prime
# Link : https://projecteuler.net/problem=7
#

def Cal():
    i = 2   # Set initial prime value
    count = 0

    while True:
        prime = True
        for j in range(2, i):
            if i % j == 0:
                prime = False
                break

        if prime == True:
            count += 1

        if count == 10001:
            break

        i = i + 1   # Update Last prime value

    return i

if __name__ == "__main__":
    print(Cal())