import random
import keyboard

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


# #task6

# def draw_func(number1, number2):

#     if type(number1) is not int or type(number2) is not int:
#         print("Entered data is not a number format")
#         return
    
#     for height in range(number2):
#         for width in range(number1):
#             print("#", end="")
#         print("#")

# draw_func(5,6)


# #task7


# def char_counter(entered_string, char):

#     if type(entered_string) is not str or type(char) is not str:
#         print("Entered data is not a str format")
#         return
    
#     count = 0

#     for character in entered_string:
#         if character == char:
#             count+=1
    
#     return count

# in_str = "John and Jane Doe"
# char = "J"

# answer = char_counter(in_str, char)
# print(f"Character '{char}' in given string: {answer} times")


# #task8


# def word_counter(countable_word):

#     if not isinstance(countable_word, str):
#         print("Error: Input must be a string format")
#         return

#     splited_words = countable_word.split()

#     return len(splited_words)

# word = "Today the weather in Tbilisi is very warm and sunny"

# print(word_counter(word))


#task9

# random_words = ["house", "water", "cat", "book", "tree", "sun", "apple", "car", "river", "ball"]
# chosen_word = random.choice(random_words)
# clue = "_" * len(chosen_word)
# attempt = 0

# print(f"You have 10 attempts to guess the word. The word is {clue}")

# while attempt != 10:

#     customer_word = input("If you want to turn off the game, enter 'exit', otherwise enter the desired character---->: ")
#     attempt += 1
    
#     if customer_word == "exit":
#         break

#     if len(customer_word) > 1:     
#         if customer_word == chosen_word:
#             clue = chosen_word
#             print(f"Congratulations, you guessed the word {chosen_word}")
#             print(f"Number of attempts: {attempt}")
#             break
#         else:
#             print("The entered word is incorrect")
#             print(f"Number of attempts: {attempt}")
#             print(f"Guess the word {clue}")
#             continue

#     if len(customer_word) == 1:
#         if not customer_word.isalpha():
#             print("Inputed word is not alphabetical, try again: ")
#             print(f"Number of attempts: {attempt}")
#             print(f"Guess the word {clue}")
#             continue

#     lowering_word = customer_word.lower()

#     if lowering_word in chosen_word:
#         for guessed_word_index, letter in enumerate(chosen_word):
#             if letter == lowering_word:
#                 clue = clue[:guessed_word_index] + lowering_word + clue[guessed_word_index + 1:]
#         if clue == chosen_word:
#             print(f"Congratulations, you guessed the word {chosen_word}")
#             print(f"Number of attempts: {attempt}")
#             break
#         print(f"Guess the word {clue}")
#         print(f"Number of attempts: {attempt}")
#         continue
#     else:
#         print("The word to guess does not contain this letter")
#         print(f"Number of attempts: {attempt}")
#         print(f"Guess the word {clue}")
#         continue

# if clue != chosen_word:
#     print(f"You lost, used attempts {attempt}. The word was: {chosen_word}")



#task10

computer_choices = ["left", "right"]
attempt_counter = 0

for attempt in range(1, 6):

    print(f"attempt {attempt}: press ← or → arrow (press 'Esc' for quit)")
    
    customer_choice = keyboard.read_key()

    while keyboard.is_pressed(customer_choice):
        pass

    comp_choice = random.choice(computer_choices)
    
    print(f"your move: {customer_choice} - computer move: {comp_choice}") 

    if comp_choice == customer_choice:
        attempt_counter += 1
    
    if customer_choice == "esc":
        break

if attempt_counter == 5:
    print(f"Congratulations, you win! - {attempt_counter} attempts guessed")
else:
    print(f"You lose! - {attempt_counter} attempts guessed")