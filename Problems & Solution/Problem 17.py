#
# Problem 17. Number letter counts
# Link : https://projecteuler.net/problem=17
#

dic = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
       11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen',
       18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy',
       80: 'eighty', 90: 'ninety', 100: 'hundred', 1000: 'thousand'}

def Cal(num):

    if num <= 20:
        return dic[num]

    elif num > 20 and num < 100:
        temp_1 = int(num/10) * 10
        temp_2 = num % 10

        if temp_2 == 0:
            return dic[num]

        else:
            return dic[temp_1] + dic[temp_2]

    elif num >= 100 and num < 1000:
        temp_1 = int(num/100)
        temp_2 = int(str(num)[1]) * 10
        temp_3 = int(str(num)[2])

        if temp_2 + temp_3 < 20 and temp_2 + temp_3 > 10:
            return dic[temp_1] + dic[100] + 'and' + dic[temp_2 + temp_3]

        elif temp_2 == 0 and temp_3 == 0:
            return dic[temp_1] + dic[100]

        elif temp_2 == 0:
            return dic[temp_1] + dic[100] + 'and' + dic[temp_3]

        elif temp_3 == 0:
            return dic[temp_1] + dic[100] + 'and' + dic[temp_2]

        else:
            return dic[temp_1] + dic[100] + 'and' + dic[temp_2] + dic[temp_3]

    if num == 1000:
            return dic[1] + dic[num]

if __name__ == "__main__":
    result = 0
    for i in range(1, 1001):
        result += len(Cal(i))
    print(result)