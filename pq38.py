number = int(input("Enter an integer: "))
number = abs(number)
total = 0
while number > 0:
    total += number % 10
    number //= 10
print("Sum of digits:", total)
