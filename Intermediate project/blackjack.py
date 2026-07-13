import random

suits = ["ყვავი", "ჯვარი", "გული", "აგური"]
values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "Ace"]


def card_value(card):
    rank = card[0]
    if rank in ["J", "Q", "K"]:
        return 10
    elif rank == "Ace":
        return 11
    else:
        return int(rank)


def get_random_card():
    rank = random.choice(values)
    suit = random.choice(suits)
    return (rank, suit)


def hand_value(hand):
    total = 0
    for card in hand:
        total += card_value(card)
    return total


def show_hand(name, hand):
    cards_text = []
    for card in hand:
        cards_text.append(f"{card[0]} {card[1]}")
    print(f"{name} კარტები: {', '.join(cards_text)} (ჯამი: {hand_value(hand)})")


def player_turn(player_hand):
    while True:
        show_hand("შენი", player_hand)
        total = hand_value(player_hand)

        if total > 21:
            print("გადააჭარბე 21-ს!")
            return

        choice = input("გინდა კარტის დამატება? (add/stop): ")

        if choice == "add":
            new_card = get_random_card()
            player_hand.append(new_card)
        elif choice == "stop":
            break
        else:
            print("გთხოვთ აკრიფოთ 'add' ან 'stop'")


def computer_turn(computer_hand):
    while hand_value(computer_hand) < 17:
        new_card = get_random_card()
        computer_hand.append(new_card)

    show_hand("კომპიუტერის", computer_hand)


def decide_winner(player_total, computer_total):
    print(f"\nშენი ჯამი: {player_total}")
    print(f"კომპიუტერის ჯამი: {computer_total}")

    if player_total > 21:
        print("თქვენ წააგეთ (გადააჭარბეთ 21-ს)")
    elif computer_total > 21:
        print("თქვენ მოიგეთ (კომპიუტერმა გადააჭარბა 21-ს)")
    elif player_total > computer_total:
        print("თქვენ მოიგეთ")
    elif computer_total > player_total:
        print("თქვენ წააგეთ")
    else:
        print("ფრეზეა - ტოლი ქულა")


def play_game():
    player_hand = [get_random_card(), get_random_card()]
    computer_hand = [get_random_card(), get_random_card()]

    print("\n===== თამაშის დაწყება =====")

    player_turn(player_hand)
    player_total = hand_value(player_hand)

    if player_total <= 21:
        print("\nკომპიუტერის ჯერია...")
        computer_turn(computer_hand)

    computer_total = hand_value(computer_hand)

    decide_winner(player_total, computer_total)


def main():
    while True:
        play_game()
        again = input("\nგინდა თავიდან თამაში? (yes/no): ")
        if again != "yes":
            print("ნახვამდის!")
            break


main()