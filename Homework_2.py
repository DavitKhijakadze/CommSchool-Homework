#task1

products_id = {
    1: "Rocket",
    2: "Ship",
    3: "Helmet"
}

products_prices = {
    1: 15000,
    2: 25000,
    3: 5000
}

selected_products = []
sum_of_proucts = 0

while True:
    print("Hello, you are in the SpaceX store, select the appropriate number to purchase the product: ")

    for product in products_id:
        print(f"{product}) {products_id[product]} - {products_prices[product]}$")

    client_response = int(input("Enter 0 to finish: "))

    if client_response == 0:
        break
    elif client_response in products_id:
        selected_products.append(client_response)
        print(f"{products_id[client_response]} added to cart")
    else:
        print("Invalid choice, try again")

for number in selected_products:
    sum_of_proucts += products_prices[number]

print(f"The total amount payable is {sum_of_proucts}$")


#task2

i = 1

while i != 20:
    if i % 2 == 0:
         print(f"{i} is Even number")
    else:
        print(f"{i} is Odd number")
    i += 1

for number in range(1,20):
    if number % 2 == 0:
         print(f"{number} is Even number")
    else:
        print(f"{number} is Odd number") 


#task3

students = {
    "Ana": [89,66,12,75,11],
    "Giorgi": [67,72,90,91,55],
    "Levant": [49,36,88,98,34],
    "Veronika": [99,88,32,65,99],
    "Nika": [77,81,41,73,99]
}

for student in students:
    average_score = sum(students[student]) / len(students[student])
    print(f"{student}'s average score is {average_score}")


#task4

while True:
    user_age = input("Please enter your age: ")
    if user_age.isdigit():
        print(f"You were born in {2026 - int(user_age)}")
        break      
    else:
        print("You entered incorrect answer, try again: ")


#task5

mylist = range(100)

number = 0

while number < len(mylist):
    square = number ** 2
    cube = number ** 3
    print(f"Square: {square} - Cube {cube}")

    number += 1