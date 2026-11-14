#Library Manager Program
books = []

while True:
    print("\n1. Add book\n2. Show books\n3. Borrow book\n4. Return book\n5. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        title = input("Book title: ").strip()
        books.append({"title": title, "available": True})
        print("Book added.")
    elif choice == "2":
        if not books:
            print("There are no books in the library.")
        for book in books:
            status = "Available" if book["available"] else "Borrowed"
            print(f"{book['title']} - {status}")
    elif choice == "3":
        title = input("Title to borrow: ").strip()
        for book in books:
            if book["title"].lower() == title.lower() and book["available"]:
                book["available"] = False
                print("Book borrowed.")
                break
        else:
            print("Book not found or already borrowed.")
    elif choice == "4":
        title = input("Title to return: ").strip()
        for book in books:
            if book["title"].lower() == title.lower() and not book["available"]:
                book["available"] = True
                print("Book returned.")
                break
        else:
            print("Borrowed book not found.")
    elif choice == "5":
        break
    else:
        print("Please enter a number from 1 to 5.")
