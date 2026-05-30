import string
import re
import random


#task1

def password_questions():

    all_in_one = []

    #პაროლის სიგრძე
    while True:
        get_pass_lenght = input("Enter the password length: ")

        if not get_pass_lenght.isdigit():
            print("Enter valid number")
            continue

        break

    #სიმბოლოების შემცველობა
    while True:
        get_symbol_answer = input("Contain symbols? (y/n): ").lower()

        if re.match(r'^[ა-ჰ\s]+$', get_symbol_answer):
            print("შეიყვანე მხოლოდ ლათინური ასოები")
            continue
        elif get_symbol_answer not in ["y", "n"]:
            print("Enter correct answer")
            continue

        if get_symbol_answer =="y":
            all_in_one.extend(list(string.punctuation))
        break

    #რიცხვების შემცველობა
    while True:
        get_digit_answer = input("Contain digits? (y/n): ").lower()

        if re.match(r'^[ა-ჰ\s]+$', get_digit_answer):
            print("Enter only in Latin")
            continue
        elif get_digit_answer not in ["y", "n"]:
            print("Enter correct answer")
            continue

        if get_digit_answer =="y":
            all_in_one.extend(list(string.digits))
        break

    #ასოების ზომა
    while True:
        get_letters_answer = input("Uppercase or lowercase? (u/l): ").lower()

        if re.match(r'^[ა-ჰ\s]+$', get_letters_answer):
            print("Enter only in Latin")
            continue
        elif get_letters_answer not in ["u", "l"]:
            print("Enter correct answer")
            continue

        if get_letters_answer =="u":
            all_in_one.extend(list(string.ascii_uppercase))
        elif get_letters_answer =="l":
            all_in_one.extend(list(string.ascii_lowercase))
        break

    generated_password = ""

    for _ in range(int(get_pass_lenght)):
        random_char = random.choice(all_in_one)
        generated_password += random_char

    return generated_password


password = password_questions()
print(f"Generated password: {password}")


#task2

def password_strength(password):

    strength_score = 0
    length = len(password)

    if length >= 12:
        strength_score += 3
    elif length >= 8:
        strength_score += 1

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    for i in range(length):
        char = password[i]

        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        else:
            has_special = True

    if has_upper:
        strength_score += 2
    if has_lower:
        strength_score += 2
    if has_digit:
        strength_score += 2
    if has_special:
        strength_score += 2

    # 4. შედეგის დაბრუნება ქულების მიხედვით
    if strength_score <= 3:
        return "weak"
    elif strength_score <= 6:
        return "medium"
    else:
        return "strong"

user_pass = password

print(f"Password strength: {password_strength(user_pass)}")

#task3

