search = int(input("Enter number to search in 1 to 5: "))
for number in range(1, 6):
    if number == search:
        print("Number found")
        break
else:
    print("Number not found")
