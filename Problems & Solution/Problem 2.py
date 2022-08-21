#
# Problem 2. Even Fibonacci numbers
# Link : https://projecteuler.net/problem=2
#

# Define 'Cal' function to calculate result value
def Cal():
    fibo = [1, 2] # Set initial Fibonacci numbers
    result = 0

    # Loop for get fibonacci numbers
    for i in range(1, 4000000):
        fibo_temp = fibo[i-1] + fibo[i]
        if fibo_temp > 4000000:
            break
        fibo.append(fibo_temp)

    # Add only Even
    for n in fibo:
        if n % 2 == 0:
            result += n

    return result

if __name__ == '__main__':
    print(Cal())