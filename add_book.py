import save_books
import random
def add_book(books):
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    isbn = random.randint(10000,99999)
    year = input("Enter the year of publication: ")
    price = input("Enter the price of the book: ")
    quantity = int(input("Enter the quantity of the book: "))

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