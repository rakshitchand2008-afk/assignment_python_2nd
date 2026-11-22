number = int(input("Enter an integer: "))
number = abs(number)
count = 1 if number == 0 else 0
while number > 0:
    count += 1
    number //= 10
print("Number of digits:", count)
