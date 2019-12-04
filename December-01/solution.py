def sevenish_number(num):
    binary = bin(num)
    result = 0
    power = 0
    for digit in binary[:1:-1]:
        result += int(digit) * 7**power
        power += 1
    print(result)
sevenish_number(10)