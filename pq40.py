start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))
for number in range(start, end + 1):
    if number >= 2:
        is_prime = True
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            print(number)
