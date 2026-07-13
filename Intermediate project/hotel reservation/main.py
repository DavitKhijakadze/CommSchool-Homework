from hotel import Hotel, Room, Customer


def create_hotel():
    hotel = Hotel("Tbilisi Grand Hotel")

    hotel.add_room(Room(101, "Single", 80, 1))
    hotel.add_room(Room(102, "Single", 80, 1))
    hotel.add_room(Room(201, "Double", 130, 2))
    hotel.add_room(Room(202, "Double", 130, 2))
    hotel.add_room(Room(301, "Suite", 250, 4))

    return hotel


def show_rooms(hotel):
    print("\n===== თავისუფალი ოთახები =====")
    rooms = hotel.show_available_rooms()

    if not rooms:
        print("სამწუხაროდ თავისუფალი ოთახები არ არის")
        return

    for room in rooms:
        print(room)


def make_booking(hotel, customer):
    show_rooms(hotel)

    room_number = int(input("\nაირჩიეთ ოთახის ნომერი: "))
    nights = int(input("რამდენი ღამით? "))

    total_price = hotel.calculate_total_booking(room_number, nights)
    print(f"\nჯამური ღირებულებაა: {total_price}₾ (ბიუჯეტი: {customer.budget}₾)")

    confirm = input("გავაგრძელოთ დაჯავშნა? (yes/no): ")

    if confirm == "yes":
        success = hotel.book_room_for_customer(customer, room_number, nights)
        if success:
            print("დაჯავშნა წარმატებით დასრულდა!")
    else:
        print("დაჯავშნა გაუქმდა")


def cancel_booking(hotel, customer):
    print(customer.show_booking_summary())
    room_number = int(input("\nრომელი ოთახის დაჯავშნის გაუქმება გსურთ? "))
    hotel.cancel_booking(customer, room_number)
    print("დაჯავშნა გაუქმდა")


def main():
    hotel = create_hotel()

    print("===== კეთილი იყოს თქვენი მობრძანება =====")
    name = input("შეიყვანეთ თქვენი სახელი: ")
    budget = float(input("შეიყვანეთ თქვენი ბიუჯეტი: "))

    customer = Customer(name, budget)

    while True:
        print("\n===== მთავარი მენიუ =====")
        print("1. თავისუფალი ოთახების ნახვა")
        print("2. ოთახის დაჯავშნა")
        print("3. ჩემი დაჯავშნების ნახვა")
        print("4. დაჯავშნის გაუქმება")
        print("5. გასვლა")

        choice = input("აირჩიეთ მოქმედება (1-5): ")

        if choice == "1":
            show_rooms(hotel)
        elif choice == "2":
            make_booking(hotel, customer)
        elif choice == "3":
            print(customer.show_booking_summary())
        elif choice == "4":
            cancel_booking(hotel, customer)
        elif choice == "5":
            print("ნახვამდის!")
            break
        else:
            print("გთხოვთ აირჩიოთ სწორი ვარიანტი (1-5)")


if __name__ == "__main__":
    main()