import random
from abc import ABC, abstractmethod



#task1

maze = [
    ["S", ".", "#", ".", "."],
    ["#", ".", "#", ".", "#"],
    [".", ".", ".", ".", "."],
    ["#", "#", "#", ".", "#"],
    [".", ".", ".", ".", "E"]
]

start_row = 0
start_col = 0

for i in range(len(maze)):
    for j in range(len(maze[i])):
        if maze[i][j] == "S":
            start_row = i
            start_col = j

row = start_row
col = start_col

while True:
    direction = input("რომელ მხარეს გინდა წასვლა? (მაღლა/დაბლა/მარცხნივ/მარჯვნივ): ")

    new_row = row
    new_col = col

    if direction == "მაღლა":
        new_row = row - 1
    elif direction == "დაბლა":
        new_row = row + 1
    elif direction == "მარცხნივ":
        new_col = col - 1
    elif direction == "მარჯვნივ":
        new_col = col + 1

    if new_row < 0 or new_row >= len(maze) or new_col < 0 or new_col >= len(maze[0]):
        print("არასწორი გზა აირჩიე! თამაში იწყება თავიდან.")
        row = start_row
        col = start_col
        continue

    if maze[new_row][new_col] == "#":
        print("არასწორი გზა აირჩიე! თამაში იწყება თავიდან.")
        row = start_row
        col = start_col
        continue

    row = new_row
    col = new_col

    if maze[row][col] == "E":
        print("შენ გაიარე ლაბირინთი!")
        break
    else:
        print("სწორად მიდიხარ!")


#task2

heroes = {
    "გიგანტი": {
        "hp": 150,
        "power": 20,
        "skills": ["მუშტის დარტყმა", "ქვის სროლა", "დაჭყლეტვა"]
    },
    "სწრაფი": {
        "hp": 90,
        "power": 15,
        "skills": ["სწრაფი დარტყმა", "ორმაგი დარტყმა", "დაცემა-გვერდზე"]
    },
    "მოქნილი": {
        "hp": 100,
        "power": 17,
        "skills": ["ჯადოსნური დარტყმა", "წყლის ტალღა", "ხტუნვა"]
    },
    "აქილევსი": {
        "hp": 120,
        "power": 25,
        "skills": ["შუბის სროლა", "ფარით დარტყმა", "გმირული იერიში"]
    },
    "პითონისტი": {
        "hp": 110,
        "power": 18,
        "skills": ["ცეცხლის სროლა", "გველის ნაკბენი", "შხამის ღრუბელი"]
    }
}


def choose_hero(player_name):
    print(f"\n{player_name}, აირჩიე გმირი:")
    hero_names = list(heroes.keys())

    for i in range(len(hero_names)):
        print(f"{i + 1}. {hero_names[i]}")

    choice = int(input("შეიყვანე ნომერი: "))
    chosen_name = hero_names[choice - 1]

    return chosen_name


def choose_skill(hero_name):
    skills = heroes[hero_name]["skills"]

    print(f"\n{hero_name}-ის სკილები:")
    for i in range(len(skills)):
        print(f"{i + 1}. {skills[i]}")

    choice = int(input("აირჩიე სკილი: "))
    return skills[choice - 1]


player1_hero = choose_hero("პირველო მოთამაშე")
player1_hp = heroes[player1_hero]["hp"]

player2_hero = choose_hero("მეორე მოთამაშე")
player2_hp = heroes[player2_hero]["hp"]

print(f"\nთამაში იწყება! {player1_hero} VS {player2_hero}\n")

while True:

    skill = choose_skill(player1_hero)
    damage = heroes[player1_hero]["power"]
    player2_hp = player2_hp - damage

    print(f"\n{player1_hero}-მა გამოიყენა '{skill}' და მიაყენა {damage} დაზიანება!")
    print(f"მეორე მოთამაშის დარჩენილი სიცოცხლე: {player2_hp}\n")

    if player2_hp <= 0:
        print(f"{player1_hero} გაიმარჯვა!")
        break

    skill = choose_skill(player2_hero)
    damage = heroes[player2_hero]["power"]
    player1_hp = player1_hp - damage

    print(f"\n{player2_hero}-მა გამოიყენა '{skill}' და მიაყენა {damage} დაზიანება!")
    print(f"პირველი მოთამაშის დარჩენილი სიცოცხლე: {player1_hp}\n")

    if player1_hp <= 0:
        print(f"{player2_hero} გაიმარჯვა!")
        break


#task3

class Earth(ABC):
    def __init__(self, name, area_km2):
        self._name = name              
        self.__area_km2 = area_km2

    def get_area(self):
        return self.__area_km2

    def set_area(self, new_area):
        if new_area > 0:
            self.__area_km2 = new_area
        else:
            print("ფართობი უნდა იყოს დადებითი რიცხვი!")

    @property
    def name(self):
        return self._name

    @abstractmethod
    def explore(self):
        pass

    def general_info(self):
        print(f"{self._name} - დედამიწის ნაწილი, ფართობი: {self.get_area()} კმ²")

class Sustainable:
    def renewable_status(self):
        print(f"{self._name} შეიძლება იყოს განახლებადი რესურსების წყარო.")

class Ocean(Earth, Sustainable): 
    def __init__(self, name, area_km2, avg_depth_m):
        super().__init__(name, area_km2)
        self.__avg_depth_m = avg_depth_m

    def explore(self):
        print(f"{self._name} ოკეანეს საშუალო სიღრმეა {self.__avg_depth_m} მეტრი. ვიკვლევთ წყალქვეშა სამყაროს.")


class Continent(Earth):
    def __init__(self, name, area_km2, population):
        super().__init__(name, area_km2)
        self.__population = population

    def explore(self):
        print(f"{self._name} კონტინენტზე ცხოვრობს დაახლოებით {self.__population} ადამიანი. ვსწავლობთ ხალხებსა და კულტურებს.")


class Atmosphere(Earth):
    def __init__(self, name, area_km2, gas_composition):
        super().__init__(name, area_km2)
        self.__gas_composition = gas_composition

    def explore(self):
        print(f"{self._name} შედგება შემდეგი გაზებისგან: {self.__gas_composition}. ვსწავლობთ ჰაერის ფენებს.")


earth_parts = [
    Ocean("წყნარი ოკეანე", 165_200_000, 4000),
    Continent("აფრიკა", 30_370_000, 1_400_000_000),
    Atmosphere("ტროპოსფერო", 510_000_000, "აზოტი, ჟანგბადი, არგონი")
]

for part in earth_parts:
    part.general_info()
    part.explore()

    if isinstance(part, Sustainable):
        part.renewable_status()

    print()


#task4

ingredients = ["ღამურა", "ბუმბული", "ვაშლი", "ყვავილი", "წყალი"]

recipes = {
    frozenset(["ღამურა", "ბუმბული"]): "ფრენის ელექსირი",
    frozenset(["ღამურა", "ვაშლი"]): "სისხლიანი ვაშლი",
    frozenset(["ღამურა", "ყვავილი"]): "ღამის ყვავილი",
    frozenset(["ღამურა", "წყალი"]): "ბნელი ნაყენი",
    frozenset(["ბუმბული", "ვაშლი"]): "ფუმფულა ჯემი",
    frozenset(["ბუმბული", "ყვავილი"]): "სუნამო",
    frozenset(["ბუმბული", "წყალი"]): "სისუფთავის წამალი",
    frozenset(["ვაშლი", "ყვავილი"]): "ყვავილოვანი წვენი",
    frozenset(["ვაშლი", "წყალი"]): "ვაშლის წვენი",
    frozenset(["ყვავილი", "წყალი"]): "ყვავილის წყალი",
}

print("ინგრედიენტები:")
for i in range(len(ingredients)):
    print(f"{i + 1}. {ingredients[i]}")

first_choice = int(input("\nაირჩიე პირველი ინგრედიენტი (ნომერი): "))
second_choice = int(input("აირჩიე მეორე ინგრედიენტი (ნომერი): "))

ingredient1 = ingredients[first_choice - 1]
ingredient2 = ingredients[second_choice - 1]

if ingredient1 == ingredient2:
    print("\nუნდა აირჩიო ორი განსხვავებული ინგრედიენტი!")
else:
    combo = frozenset([ingredient1, ingredient2])
    result = recipes[combo]
    print(f"\n{ingredient1} + {ingredient2} = {result}")


#task5

class Transport(ABC):
    def __init__(self, fuel, speed, capacity):
        self.__fuel = fuel      
        self.speed = speed
        self.capacity = capacity

    def get_fuel(self):
        return self.__fuel

    def set_fuel(self, amount):
        if amount >= 0:
            self.__fuel = amount
        else:
            print("საწვავი ვერ იქნება უარყოფითი!")

    def refuel(self, amount):
        self.__fuel += amount
        print(f"დაემატა {amount} ლიტრი საწვავი. ახლა საწვავია: {self.__fuel}")

    @abstractmethod
    def move(self):
        pass

    def use_fuel(self, amount):
        if self.__fuel >= amount:
            self.__fuel -= amount
        else:
            print("საწვავი საკმარისი არ არის! ტრანსპორტი ჩერდება.")
            self.__fuel = 0


class Car(Transport):
    def move(self):
        fuel_needed = 5
        self.use_fuel(fuel_needed)
        print(f"მანქანა მოძრაობს {self.speed} კმ/სთ სიჩქარით და ხარჯავს {fuel_needed} ლიტრს. დარჩენილი საწვავი: {self.get_fuel()}")


class Bus(Transport):
    def move(self):
        fuel_needed = 10 + (self.capacity // 10)
        self.use_fuel(fuel_needed)
        print(f"ავტობუსი მოძრაობს {self.speed} კმ/სთ სიჩქარით და ხარჯავს {fuel_needed} ლიტრს. დარჩენილი საწვავი: {self.get_fuel()}")


class Bike(Transport):
    def move(self):
        fuel_needed = 0
        print(f"ველოსიპედი მოძრაობს {self.speed} კმ/სთ სიჩქარით და საწვავს არ საჭიროებს. დარჩენილი საწვავი: {self.get_fuel()}")

transports = [
    Car(fuel=20, speed=120, capacity=4),
    Bus(fuel=50, speed=80, capacity=40),
    Bike(fuel=0, speed=25, capacity=1)
]

for t in transports:
    t.move()
    print()