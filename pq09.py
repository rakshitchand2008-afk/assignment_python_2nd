number = int(input("Enter an integer: "))
last_digit = number - (number // 10 * 10)
print("Last digit:", last_digit)
