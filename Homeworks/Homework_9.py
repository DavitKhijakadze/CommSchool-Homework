import random

#task1

class Character:
    def __init__(self, name, hp, strength):
        self.name = name
        self.hp = hp
        self.strength = strength

    def attack(self, other):
        if isinstance(self, Warrior) and isinstance(other, Mage):
            print(f"{self.name} (Warrior) ამარცხებს {other.name}-ს (Mage)!")
        elif isinstance(self, Mage) and isinstance(other, Archer):
            print(f"{self.name} (Mage) ამარცხებს {other.name}-ს (Archer)!")
        elif isinstance(self, Archer) and isinstance(other, Warrior):
            print(f"{self.name} (Archer) ამარცხებს {other.name}-ს (Warrior)!")
        else:
            print(f"{self.name} ვერ დაამარცხა {other.name}")

class Warrior(Character):
    def __init__(self, name, hp, strength):
        super().__init__(name, hp, strength)

class Mage(Character):
    def __init__(self, name, hp, strength):
        super().__init__(name, hp, strength)

class Archer(Character):
    def __init__(self, name, hp, strength):
        super().__init__(name, hp, strength)

w = Warrior("გელა", 100, 20)
m = Mage("ანი", 80, 15)
a = Archer("გიო", 90, 18)

w.attack(m)  
m.attack(a)  
a.attack(w)


#task2


class Monster:
    def __init__(self, name, monster_type):
        self.name = name
        self.type = monster_type

    @classmethod
    def create_from_level(cls, level):
        if level <= 3:
            return cls("ფუმფულა", "დათუნია")
        elif level <= 6:
            return cls("მხიარული", "კუ")
        else:
            return cls("ბრძენი", "ბუ")

monsters = []

for i in range(1, 11):
    monsters.append(Monster.create_from_level(i))

for m in monsters:
    print(f"მონსტრი: {m.name} ({m.type})")


#task3

class SlotMachine:
    def __init__(self, symbols):
        self.symbols = symbols

    @staticmethod
    def get_random_symbol():
        return random.choice(["🍒", "🍋", "🔔", "⭐"])

    @classmethod
    def from_difficulty(cls, level):
        return cls(["🍒", "🍋", "🔔", "⭐", "💎"][:level + 2])

    def play(self):
        spin = []
        for _ in range(3):
            spin.append(self.get_random_symbol()) 
        print(f"შედეგი: {spin}")
        return spin[0] == spin[1] == spin[2]

slot = SlotMachine.from_difficulty(2)

if slot.play():
    print("მოგება:")
else:
    print("წაგება")


#task4

class Hero:
    def __init__(self, name):
        self.__health = 100
        self.__score = 0
        self.name = name

    @staticmethod
    def random_event():
        return random.choice([("ქულა", 10), ("დაზიანება", -20)])

    @classmethod
    def from_name(cls, name):
        return cls(name)

    def play(self):
        while self.__health > 0:
            event, val = self.random_event()
            if event == "ქულა": self.__score += val
            else: self.__health += val
            print(f"{self.name}: HP={self.__health}, Score={self.__score}")

class SuperHero(Hero):
    def __init__(self, name, power):
        super().__init__(name)
        self.power = power

h = Hero.from_name("არტურ")
h.play()


#task5

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return f"{self.rank}{self.suit}"

class Deck:
    def __init__(self):
        self.__cards = []

    @classmethod
    def create_standard_deck(cls):
        new_deck = cls()
        suits = ['♠', '♥', '♦', '♣']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        
        all_cards = []
        for s in suits:
            for r in ranks:
                card = Card(r, s)
                all_cards.append(card)
        
        new_deck.__cards = all_cards
        return new_deck

    @staticmethod
    def shuffle(cards):
        random.shuffle(cards)

    def draw(self, n):
        hand = []
        for i in range(n):
            if len(self.__cards) > 0:
                card = self.__cards.pop()
                hand.append(card)
        return hand

my_deck = Deck.create_standard_deck()
all_cards_list = my_deck.draw(52) 
Deck.shuffle(all_cards_list)

hand = all_cards_list[:5]
print(f"მოთამაშის ხელშია: {hand}")

ranks = []
for c in hand:
    ranks.append(c.rank)

is_pair = False
for i in range(len(ranks)):
    for j in range(i + 1, len(ranks)):
        if ranks[i] == ranks[j]:
            is_pair = True

if is_pair:
    print("შედეგი: გაქვს წყვილი ან მეტი")
else:
    print("შედეგი: კომბინაცია არ არის")