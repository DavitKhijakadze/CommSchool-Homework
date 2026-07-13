library = [
    {"title": "ვეფხისტყაოსანი", "author": "შოთა რუსთაველი", "year": 1180},
    {"title": "დათა თუთაშხია", "author": "ჭაბუა ამირეჯიბი", "year": 1975},
    {"title": "Harry Potter", "author": "J.K. Rowling", "year": 1997},
    {"title": "1984", "author": "George Orwell", "year": 1949},
    {"title": "The Hobbit", "author": "J.R.R. Tolkien", "year": 1937},
    {"title": "Sapiens", "author": "Yuval Noah Harari", "year": 2011},
    {"title": "Crime and Punishment", "author": "Fyodor Dostoevsky", "year": 1866},
    {"title": "Kartlis Tskhovreba", "author": "Various", "year": 1200},
    {"title": "The Alchemist", "author": "Paulo Coelho", "year": 1988},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
]


def show_books():
    print("\n--- ბიბლიოთეკაში არსებული წიგნები ---")
    for i in range(len(library)):
        book = library[i]
        print(f"{i + 1}. {book['title']} - {book['author']} ({book['year']})")
    print("--------------------------------------")


def add_book():
    print("\nჩაწერეთ წიგნის სახელი/ავტორი და წელი")
    title = input("სათაური: ")
    author = input("ავტორი: ")
    year = int(input("წელი: "))

    new_book = {"title": title, "author": author, "year": year}
    library.append(new_book)
    print(f"წიგნი '{title}' დაემატა ბიბლიოთეკას!")


def search_book():
    search_title = input("\nჩაწერეთ საძიებო სათაური: ")
    found = False
    for book in library:
        if book["title"] == search_title:
            print(f"ნაპოვნია: {book['title']} - {book['author']} ({book['year']})")
            found = True
            break
    if not found:
        print("ასეთი წიგნი ბიბლიოთეკაში არ მოიძებნა.")


def take_book():
    show_books()
    choice = int(input("\nაირჩიეთ წიგნის ნომერი წასაკითხად: "))
    index = choice - 1

    if 0 <= index < len(library):
        book = library.pop(index)
        print(f"თქვენ გაიტანეთ წიგნი: {book["title"]} - {book["author"]}")
    else:
        print("ასეთი ნომერი არ არსებობს.")


def main():
    while True:
        print("\n===== მინი ბიბლიოთეკა =====")
        print("1. წიგნების სია")
        print("2. წიგნის დამატება")
        print("3. წიგნის ძებნა სათაურით")
        print("4. წიგნის აღება წასაკითხად")
        print("5. გასვლა")

        choice = input("აირჩიეთ მოქმედება (1-5): ")

        if choice == "1":
            show_books()
        elif choice == "2":
            add_book()
        elif choice == "3":
            search_book()
        elif choice == "4":
            take_book()
        elif choice == "5":
            print("ნახვამდის!")
            break
        else:
            print("გთხოვთ აირჩიოთ სწორი ვარიანტი (1-5)")


main()