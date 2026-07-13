import unittest


class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(4, 3), 12)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)


class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Deposit amount cannot be negative")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount
        return self.balance


class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount(100)

    def test_deposit_correct_balance(self):
        self.account.deposit(50)
        self.assertEqual(self.account.balance, 150)

    def test_deposit_negative_amount(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-50)

    def test_withdraw_more_than_balance(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(200)

    def test_withdraw_correct_balance(self):
        self.account.withdraw(50)
        self.assertEqual(self.account.balance, 50)


def get_status(response):
    if "status" not in response:
        raise KeyError("status not found in response")
    return response["status"]


class TestGetStatus(unittest.TestCase):
    def test_get_status_existing(self):
        response = {"status": "ok", "code": 200}
        self.assertEqual(get_status(response), "ok")

    def test_get_status_missing(self):
        response = {"code": 404}
        with self.assertRaises(KeyError):
            get_status(response)


if __name__ == "__main__":
    unittest.main()
