import save_books
def add_book(books):
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    isbn = input("Enter the ISBN of the book: ")
    year = input("Enter the year of publication: ")
    price = input("Enter the price of the book: ")
    quantity = input("Enter the quantity of the book: ")

    book = {
        "title": title,
        "author": author,
        "isbn": isbn,
        "year": year,
        "price": price,
        "quantity": quantity
    }
    books.append(book)
    save_books.save_books(books)
    print("Book added successfully!")