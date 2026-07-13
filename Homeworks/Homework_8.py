from dataclasses import dataclass


#task1

class BankAccount:
    def __init__(self, owner, balance):
        self.__owener = owner
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("not enough money on balance")
    
    def get_balance(self):
        return self.__balance
    

account = BankAccount("Giorgi", 1000)
account.deposit(500)
account.withdraw(200)
print(account.get_balance())


#task2

class ShoppingCart:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)
    
    def __eq__(self, value):
        return len(self) == len(value)
        
cart1 = ShoppingCart(["milk", "bread"])
cart2 = ShoppingCart(["apple", "banana"])
cart3 = ShoppingCart(["juice", "water"])
cart4 = ShoppingCart(["meat", "cheese"])

print(cart1 == cart2)
print(cart1 == cart2 == cart3)
print(cart1 == cart2 == cart3 == cart4)


#task3


@dataclass
class Book:
    title: str
    author: str
    year: int

    def is_classic(self):
        return self.year < 1970

book1 = Book("The Hobbit", "Tolkien", 1937)
book2 = Book("Harry Potter", "Rowling", 1997)

print(book1.is_classic())
print(book2.is_classic())


#task4

class Person:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print("Person removed")

p1 = Person("Luka")
del p1


#task5

class Temperature:
    def __init__(self, celsius):
        self.__celsius = celsius 

    @property
    def celsius(self):
        return self.__celsius

    @celsius.setter
    def celsius(self, value):
        self.__celsius = value

    @property
    def fahrenheit(self):
        return self.__celsius * 9 / 5 + 32

temp = Temperature(25)
print(temp.fahrenheit)

temp.celsius = 30
print(temp.fahrenheit)


#task6

class CustomList:
    def __init__(self, elements):
        self.elements = elements

    def __getitem__(self, index):
        return self.elements[index]

    def __setitem__(self, index, value):
        self.elements[index] = value

    def __iter__(self):
        return iter(self.elements)

my_list = CustomList([10, 20, 30])
my_list[1] = 99

for item in my_list:
    print(item)


#task7

class Refrigerator:
    def __init__(self, items):
        self.items = items

    def __contains__(self, item):
        return item in self.items

    def __str__(self):
        return f"Fridge with {len(self.items)} items"

    def __del__(self):
        print("Fridge unplugged!")

fridge = Refrigerator(["milk", "cheese", "butter"])
print("milk" in fridge)
print(fridge)
del fridge


#task8

class FunnyCalculator:
    def __add__(self, other):
        return "Why are you adding numbers? Just buy a calculator"

    def __mul__(self, other):
        return "Multiplication is too mainstream"

    def __truediv__(self, other):
        if other == 0:
            print("ZeroDivisionError? Nah, let’s just say infinity")
            return
        return "Just a normal division"

    def __rtruediv__(self, other):
        return "Why are you dividing something by a calculator"

    def __str__(self):
        return "I’m the funniest calculator in Python!"

calc = FunnyCalculator()
print(calc + 5)
print(calc * 2)
print(10 / calc)
calc / 0