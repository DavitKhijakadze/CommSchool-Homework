
import unittest
from hotel import Room, Customer, Hotel


class TestCustomer(unittest.TestCase):

    def test_pay_for_booking_success(self):
        customer = Customer("Giorgi", 500)
        result = customer.pay_for_booking(300)

        self.assertTrue(result)
        self.assertEqual(customer.budget, 200)

    def test_pay_for_booking_not_enough_money(self):
        customer = Customer("Giorgi", 100)
        result = customer.pay_for_booking(300)

        self.assertFalse(result)
        self.assertEqual(customer.budget, 100)  # ბიუჯეტი არ უნდა შეიცვალოს


class TestHotel(unittest.TestCase):

    def setUp(self):
        # ეს მეთოდი ავტომატურად გაეშვება ყოველი ტესტის წინ
        self.hotel = Hotel("Test Hotel")
        self.room = Room(101, "Single", 100, 1)
        self.hotel.add_room(self.room)
        self.customer = Customer("Nino", 1000)

    def test_book_room_success(self):
        result = self.hotel.book_room_for_customer(self.customer, 101, 2)

        self.assertTrue(result)
        self.assertFalse(self.room.is_available)

    def test_cannot_book_already_booked_room(self):
        self.hotel.book_room_for_customer(self.customer, 101, 2)

        second_customer = Customer("Levan", 1000)
        result = self.hotel.book_room_for_customer(second_customer, 101, 1)

        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()