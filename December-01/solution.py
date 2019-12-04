def sevenish_number(num):
    binary = bin(num)[2:]
    result = 0
    power = 0
    for digit in reversed(binary):
        result += int(digit) * 7**power
        power += 1
    return result
print(sevenish_number(10))