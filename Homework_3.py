#task1

while True:

    char = input("Please enter any char: ")

    if len(char) > 1:
        print("Enter 1 letter: ")   
        print(15 * "=")

    elif not char.isalpha():
        print("This is not alphabet, try again: ")
        print(15 * "=")

    elif char.lower() in "aeiou":
        print(f"{char} is a vowel")
        print(15 * "=")
        break

    else:
        print(f"{char} is a consonant")
        print(15 * "=")
        break


#task2

for i in range(10,0,-1):
    print(i, end=" ")


#task3