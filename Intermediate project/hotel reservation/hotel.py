import logging
from datetime import datetime

# ლოგირების კონფიგურაცია - ყველა დაჯავშნა/გაუქმება ჩაიწერება ფაილში
logging.basicConfig(
    filename="hotel_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    encoding="utf-8"
)


def get_season_multiplier():
    # ფასის დინამიური ცვლილება სეზონის მიხედვით
    month = datetime.now().month

    if month in [6, 7, 8]:
        return 1.3  # ზაფხულის სეზონი - ძვირი
    elif month == 12:
        return 1.2  # საახალწლო სეზონი - ძვირი
    else:
        return 1.0  # ჩვეულებრივი სეზონი


class Room:
    def __init__(self, room_number, room_type, price_per_night, max_guests):
        self.room_number = room_number
        self.room_type = room_type
        self.price_per_night = price_per_night
        self.max_guests = max_guests
        self.is_available = True

    def book_room(self):
        self.is_available = False

    def release_room(self):
        self.is_available = True

    def calculate_price(self, nights):
        multiplier = get_season_multiplier()
        return self.price_per_night * nights * multiplier

    def __str__(self):
        status = "თავისუფალია" if self.is_available else "დაკავებულია"
        return f"ოთახი #{self.room_number} ({self.room_type}) - {self.price_per_night}₾/ღამე - მაქს. {self.max_guests} სტუმარი - {status}"


class Customer:
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget
        self.booked_rooms = []
        self.reward_points = 0

    def add_room(self, room):
        self.booked_rooms.append(room)

    def remove_room(self, room):
        if room in self.booked_rooms:
            self.booked_rooms.remove(room)

    def pay_for_booking(self, total_price):
        if total_price > self.budget:
            return False

        self.budget -= total_price
        self.reward_points += int(total_price // 100)  # ყოველ 100 ლარზე 1 ქულა
        return True

    def show_booking_summary(self):
        if not self.booked_rooms:
            return f"{self.name}-ს არ აქვს დაჯავშნილი ოთახები"

        summary = f"\n{self.name}-ის დაჯავშნები:\n"
        for room in self.booked_rooms:
            summary += f"  - {room}\n"
        summary += f"დარჩენილი ბიუჯეტი: {self.budget}₾\n"
        summary += f"დაგროვილი ქულები: {self.reward_points}\n"
        return summary


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.bookings_log = []

    def add_room(self, room):
        self.rooms.append(room)

    def find_room(self, room_number):
        for room in self.rooms:
            if room.room_number == room_number:
                return room
        return None

    def show_available_rooms(self, room_type=None):
        available = []
        for room in self.rooms:
            if room.is_available:
                if room_type is None or room.room_type == room_type:
                    available.append(room)
        return available

    def calculate_total_booking(self, room_number, nights):
        room = self.find_room(room_number)
        if room is None:
            return 0
        return room.calculate_price(nights)

    def book_room_for_customer(self, customer, room_number, nights):
        room = self.find_room(room_number)

        if room is None:
            print("ასეთი ოთახი არ არსებობს")
            return False

        if not room.is_available:
            print("ეს ოთახი უკვე დაკავებულია")
            return False

        total_price = self.calculate_total_booking(room_number, nights)

        if not customer.pay_for_booking(total_price):
            print("არასაკმარისი ბიუჯეტია ამ დაჯავშნისთვის")
            return False

        room.book_room()
        customer.add_room(room)
        self.log_booking(customer, room, total_price)
        return True

    def log_booking(self, customer, room, total_price):
        message = f"დაჯავშნა: {customer.name} დაჯავშნა ოთახი #{room.room_number} ({room.room_type}) - სულ: {total_price}₾"
        self.bookings_log.append(message)
        logging.info(message)

    def cancel_booking(self, customer, room_number):
        room = self.find_room(room_number)

        if room is None:
            print("ასეთი ოთახი არ არსებობს")
            return False

        room.release_room()
        customer.remove_room(room)

        message = f"გაუქმება: {customer.name}-მა გააუქმა ოთახი #{room.room_number}"
        self.bookings_log.append(message)
        logging.info(message)

        return True