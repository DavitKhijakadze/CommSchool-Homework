# წინასწარ შენახული მონაცემები
email = "user@mail.com"
nickname = "george777"
password = "password123"


def check_name(name):
    if name == "":
        print("ცარიელი ველი დაუშვებელია, შემოიტანეთ სახელი")
        return False

    if name.isdigit():
        print("შემოყვანილია რიცხვითი მნიშვნელობა, შემოიტანეთ მხოლოდ string პატარა რეგისტრში")
        return False

    if not name.isalnum():
        print("შემოყვანილია სიმბოლოები, შემოიტანეთ მხოლოდ string პატარა რეგისტრში")
        return False

    if not name.isascii():
        print("შემოყვანილია სხვა ენის სიმბოლოები, შემოიტანეთ მხოლოდ ლათინური ასოები")
        return False

    if name.isupper():
        print("შემოყვანილია დიდი რეგისტრის ასოები, შემოიტანეთ მხოლოდ პატარა ასოები")
        return False

    if not name.islower():
        print("შემოყვანილია შერეული რეგისტრის ასოები, შემოიტანეთ მხოლოდ პატარა ასოები")
        return False
    
    return True


def register_user(name):
    print("\n===== რეგისტრაცია წარმატებით დასრულდა =====")
    print(f"ელ-ფოსტა: {email}")
    print(f"სახელი: {name}")
    print(f"ზედმეტსახელი: {nickname}")
    print(f"პაროლი: {password}")


def main():
    print("===== რეგისტრაციის გვერდი =====")

    while True:
        name = input("შემოიყვანეთ სახელი: ")

        if check_name(name):
            register_user(name)
            break
        else:
            print("სცადეთ თავიდან\n")


main()