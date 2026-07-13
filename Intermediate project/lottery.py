import random
from datetime import datetime

JACKPOT = 1000000


def log_result(player_numbers, winning_numbers, matches, prize):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"[{now}] მოთამაშის რიცხვები: {player_numbers} | გათამაშების რიცხვები: {winning_numbers} | დამთხვევები: {matches} | მოგება: {prize} ₾\n"

    with open("lottery_log.txt", "a", encoding="utf-8") as log_file:
        log_file.write(log_line)


def generate_winning_numbers():
    numbers = []
    while len(numbers) < 6:
        number = random.randint(1, 49)
        if number not in numbers:
            numbers.append(number)
    return numbers


def get_player_numbers():
    player_numbers = []
    print("\nჩაწერეთ თქვენი 6 რიცხვი (1-49):")
    for i in range(6):
        number = int(input(f"რიცხვი #{i + 1}: "))
        player_numbers.append(number)
    return player_numbers


def count_matches(player_numbers, winning_numbers):
    matches = 0
    for number in player_numbers:
        if number in winning_numbers:
            matches += 1
    return matches


def calculate_prize(matches):
    if matches == 6:
        return JACKPOT
    elif matches == 5:
        return JACKPOT - (JACKPOT * 0.4)
    elif matches == 4:
        return JACKPOT - (JACKPOT * 0.6)
    elif matches == 3:
        return JACKPOT - (JACKPOT * 0.8)
    else:
        return 0


def play_lottery():
    player_numbers = get_player_numbers()
    winning_numbers = generate_winning_numbers()

    print(f"\nგათამაშების რიცხვებია: {winning_numbers}")

    matches = count_matches(player_numbers, winning_numbers)
    prize = calculate_prize(matches)

    print(f"თქვენ დაგემთხვათ {matches} რიცხვი")

    if prize > 0:
        print(f"გილოცავთ! თქვენ მოიგეთ {prize} ₾")
    else:
        print("სამწუხაროდ, მოგება არ გაქვთ")

    log_result(player_numbers, winning_numbers, matches, prize)


def main():
    while True:
        play_lottery()
        again = input("\nგინდა თავიდან თამაში? (yes/no): ")
        if again != "yes":
            print("ნახვამდის!")
            break


main()