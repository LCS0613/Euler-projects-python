#
# Problem 5. Smallest multiple
# Link : https://projecteuler.net/problem=5
#

def Cal():
    i = 1

    while True:
        temp = []
        for j in range(1, 21):
            if i / j >= 1 and i % j == 0:
                temp.append(1)
            else:
                break
        if len(temp) == 20:
            break
        i = i + 1

    return i

if __name__ == "__main__":
    print(Cal())