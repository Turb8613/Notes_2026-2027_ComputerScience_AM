for number in range(10001):
    digits = str(number)
    if digits == digits[::-1]: print(number)