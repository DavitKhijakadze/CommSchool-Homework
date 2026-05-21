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

