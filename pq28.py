character = input("Enter a character: ").lower()
if len(character) == 1:
    if character in "aeiou":
        print("Vowel")
    elif character.isalpha():
        print("Consonant")
    else:
        print("Not a letter")
else:
    print("Please enter exactly one character")
