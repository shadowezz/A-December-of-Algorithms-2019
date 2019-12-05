import math
def is_prime(number):
    if (number < 2):
        return False
    else:
        root = math.floor(math.sqrt(number))
        for num in range(2, root + 1):
            if (number % num == 0):
                return False
        return True

def fibprime(number):
    def helper(prev, current, number):
        if (is_prime(current)):
            if (number == 1):
                print(current)
            else:
                print(current, end=", ")
            number -= 1
        if (number != 0):
            return helper(current, prev + current, number)
    return helper(1, 2, number)

fibprime(5)