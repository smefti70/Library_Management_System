import add_book
import view_books
import update_book
import delete_book
import load_books
import lend_book
import return_book

books = load_books.load_books()
while True:
    print("\nLibrary Management System")
    print("1. Add a Book")
    print("2. View All Books")
    print("3. Update Book Details")
    print("4. Delete a Book")
    print("5. Lend a Book")
    print("6. Return a Book")
    print("0. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_book.add_book(books)

    elif choice == 2:
        if not books:
            print("No books available")
        else:
            view_books.view_books()

    elif choice == 3:
        if not books:
            print("No books available")
        else:
            view_books.view_books()
            book_id = int(input("Enter the book ID to be updated: "))
            update_book.update_book(books,book_id)

    elif choice == 4:
        view_books.view_books()
        if not books:
            print("No books available")
        else:
            book_id = int(input("Enter the book ID to be deleted: "))
            delete_book.delete_book(books,book_id)

    elif choice == 5:
        view_books.view_books()
        book_id = int(input('Enter ISBN number of the book you want to lend: '))
        lend_book.lend_book(books,book_id)



    elif choice == 6:
        view_books.view_books()  # Show the list of books
        book_id = int(input('Enter ISBN number of the book you want to return: '))  # Convert to int
        borrower_name = input('Enter the name of the borrower: ')
        return_book.return_book(books, book_id, borrower_name)


    elif choice == 0:
        print("\nThanks for using Library Management System.")
        break

    else:
        print("Invalid choice. Please try again with valid input.")