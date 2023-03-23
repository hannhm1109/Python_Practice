number = 7536

print("Number we got : ", number)
while number > 0:
    digit = number % 10
    number = number // 10
    print(digit, end=" ")