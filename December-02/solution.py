def is_valid_credit_card(number):
    reversed = str(number)[::-1]
    is_odd = 0
    even_sum = 0
    odd_sum = 0
    for digit in reversed:
        if (is_odd % 2 == 0):
            odd_sum += int(digit)
            is_odd = 1
        else:
            twice = 2 * int(digit)
            sum_digits = twice % 10 + twice // 10
            even_sum += sum_digits
            is_odd = 0
    total = even_sum + odd_sum
    return total % 10 == 0
print(is_valid_credit_card(49))

