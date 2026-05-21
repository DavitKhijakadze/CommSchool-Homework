#task1

products_id = {
    1: "rocket",
    2: "ship",
    3: "helmet"
}

products_prices = {
    1: 15000,
    2: 25000,
    3: 5000
}

Selected_products = []
sum_of_proucts = 0

while True:
    print("Hello, you are in the SpaceX store, select the appropriate number to purchase the product: ")

    for product in products_id:
        print(f"{product}) {products_id[product]} - {products_prices[product]}$")

    client_response = int(input("Enter 0 to finish: "))

    if client_response == 0:
        break
    elif client_response in products_id:
        Selected_products.append(client_response)
        print(f"{products_id[client_response]} added to cart")
    else:
        print("invalid choice, try again")

for number in Selected_products:
    sum_of_proucts += products_prices[number]

print(f"The total amount payable is {sum_of_proucts}$")