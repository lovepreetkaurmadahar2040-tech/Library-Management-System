books = {}
issued_books = []

def add_book():
    name = input("Enter the name of book: ")
    if name in books:
        books[name] += 1
    else:
        books[name] = 1
    print(name, 'is added')

def show_books():
    if len(books) == 0:
        print("No books available")
    else:
        print("Available books:")
        for b, qty in books.items():
            print(b, "- Quantity:", qty)

def borrow_book():
    name = input("Enter book name: ")
    
    if name in books and books[name] > 0:
        student = input("Enter student name: ")
        date = input("Enter issue date (YYYY-MM-DD): ")
        duration = int(input("Enter duration (days): "))

        record = {
            "book": name,
            "student": student,
            "date": date,
            "duration": duration
        }

        issued_books.append(record)
        books[name] -= 1

        print(name, "issued to", student)

    else:
        print("Book not available")

def show_issued_books():
    if len(issued_books) == 0:
        print("No books issued")
    else:
        print("\nIssued Books:")
        for r in issued_books:
            print("Book:", r["book"])
            print("Student:", r["student"])
            print("Date:", r["date"])
            print("Duration:", r["duration"], "days")
            print("------")

def return_book():
    name = input("Enter book name: ")
    student = input("Enter student name: ")

    for r in issued_books:
        if r["book"] == name and r["student"] == student:
            issued_books.remove(r)
            books[name] += 1
            print("Book returned successfully")
            return

    print("Record not found")

def library():
    while True:
        print("\nMenu")
        print("1. Add book")
        print("2. Show books")
        print("3. Issue book")
        print("4. Show issued books")
        print("5. Return book")
        print("6. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            add_book()
        elif choice == 2:
            show_books()
        elif choice == 3:
            borrow_book()
        elif choice == 4:
            show_issued_books()
        elif choice == 5:
            return_book()
        elif choice == 6:
            print("Thank you!")
            break
        else:
            print("Invalid choice")

library()
