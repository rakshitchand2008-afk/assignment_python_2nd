number = int(input("Enter a two-digit number: "))
tens = number // 10
ones = number - (tens * 10)
print("Sum of digits:", tens + ones)
