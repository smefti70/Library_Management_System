import save_books
def update_book(books, book_id):
    for book in books:
        if book['isbn'] == str(book_id):
            print("What would you like to update?\n(title, author, year, price, quantity, all)")
            choice = input("Enter your choice: ")
            choice = choice.lower()

            if choice == 'title':
                book['title'] = input("Enter the new title: ")
            elif choice == 'author':
                book['author'] = input("Enter the new author: ")
            elif choice == 'year':
                book['year'] = input("Enter the new year: ")
            elif choice == 'price':
                book['price'] = input("Enter the new price: ")
            elif choice == 'quantity':
                book['quantity'] = input("Enter the new quantity: ")
            elif choice == 'all':
                book['title'] = input("Enter the new title: ")
                book['author'] = input("Enter the new author: ")
                book['year'] = input("Enter the new year: ")
                book['price'] = input("Enter the new price: ")
                book['quantity'] = input("Enter the new quantity: ")
            else:
                print("Invalid choice")
            save_books.save_books(books)
            print("Book updated successfully")
            return