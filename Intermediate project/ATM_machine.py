from datetime import datetime

balance = 5000


def log_operation(operation, amount):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"[{now}] {operation}: {amount} ₾ (ბალანსი: {balance} ₾)\n"

    with open("atm_log.txt", "a", encoding="utf-8") as log_file:
        log_file.write(log_line)


def show_balance():
    print(f"\nთქვენი ბალანსია: {balance} ₾")


def deposit():
    global balance
    amount = float(input("რამდენის შემოტანა გსურთ? "))

    if amount > 1000:
        print("ერთჯერადად ვერ შეიტანთ 1000 ₾-ზე მეტს!")
        return

    balance += amount
    print(f"წარმატებით შეიტანეთ {amount} ₾")
    log_operation("შემოტანა", amount)


def withdraw():
    global balance
    amount = float(input("რამდენის გატანა გსურთ? "))

    if amount > balance:
        print("არასაკმარისი თანხაა ანგარიშზე!")
        return

    balance -= amount
    print(f"წარმატებით გაიტანეთ {amount} ₾")
    log_operation("გატანა", amount)


def main():
    while True:
        print("\n===== ბანკომატი =====")
        print("1. ბალანსის ნახვა")
        print("2. თანხის შემოტანა")
        print("3. თანხის გატანა")
        print("4. გასვლა")

        choice = input("აირჩიეთ მოქმედება (1-4): ")

        if choice == "1":
            show_balance()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            print("ნახვამდის!")
            break
        else:
            print("გთხოვთ აირჩიოთ სწორი ვარიანტი (1-4)")


main()