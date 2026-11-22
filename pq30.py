units = int(input("Enter electricity units consumed: "))
if units <= 100:
    charge = units * 5
else:
    if units <= 200:
        charge = 100 * 5 + (units - 100) * 7
    else:
        if units <= 300:
            charge = 100 * 5 + 100 * 7 + (units - 200) * 10
        else:
            charge = 100 * 5 + 100 * 7 + 100 * 10 + (units - 300) * 15
print("Electricity charge:", charge)
