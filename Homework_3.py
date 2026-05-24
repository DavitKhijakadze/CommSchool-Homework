import random


# #task1

# while True:

#     char = input("Please enter any char: ")

#     if len(char) > 1:
#         print("Enter 1 letter: ")   
#         print(15 * "=")

#     elif not char.isalpha():
#         print("This is not alphabet, try again: ")
#         print(15 * "=")

#     elif char.lower() in "aeiou":
#         print(f"{char} is a vowel")
#         print(15 * "=")
#         break

#     else:
#         print(f"{char} is a consonant")
#         print(15 * "=")
#         break


# #task2

# for i in range(10,0,-1):
#     print(i, end=" ")


# #task3

# lst = [random.randint(1, 20) for _ in range(10)]
# indexed_lst = list(enumerate(lst))
# sorted_index = sorted(indexed_lst, key=lambda x: x[1], reverse=True)

# for original_index, value in sorted_index[:3]:
#     print(f"data {value} - index {original_index}")

# print(f"Main list: {lst}")


# #task4


# inputed_width = None
# inputed_height = None

# while True:

#     inputed_digit1 = input("Please enter any number for width: ")
#     inputed_digit2 = input("Please enter any number for height: ")

#     if not inputed_digit1.isdigit() or not inputed_digit2.isdigit():
#         print("Entered data is not a number, please try again: ")
#         continue
    
#     inputed_width = int(inputed_digit1)
#     inputed_height = int(inputed_digit2)

#     for height in range(inputed_height):
#         for width in range(inputed_width):
#             print("#", end="")
#         print("#")
    
#     break


# #task5


# def my_calc(number1, number2):

#     if type(number1) is not int or type(number2) is not int:
#         print("Entered data is not a number format")
#         return

#     print(f"Add:       {number1} + {number2} = {number1 + number2}")
#     print(f"Subtract:    {number1} - {number2} = {number1 - number2}")
#     print(f"Multiply: {number1} * {number2} = {number1 * number2}")
#     print(f"Divide:       {number1} / {number2} = {number1 / number2}")
#     print(f"Floor Divide: {number1} // {number2} = {number1 // number2}")
#     print(f"Modulus:        {number1} % {number2} = {number1 % number2}")
    
# my_calc(4,2)