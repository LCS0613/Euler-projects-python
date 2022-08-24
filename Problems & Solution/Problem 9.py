#
# Problem 9. Special Pythagorean triplet
# Link : https://projecteuler.net/problem=9
#

def Cal():
    for a in range(1, 1000):
        for b in range(1, 1000):
            for c in range(1, 1000):
                if a + b + c == 1000 and a ** 2 + b ** 2 == c ** 2:
                    break
            if a + b + c == 1000 and a ** 2 + b ** 2 == c ** 2:
                break
        if a + b + c == 1000 and a ** 2 + b ** 2 == c ** 2:
            break
    return a * b * c

if __name__ == "__main__":
    print(Cal())