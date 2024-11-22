import save_books
def lend_book(books, book_id):
    for book in books:
        if book['isbn'] == str(book_id):
            if int(book['quantity']) > 0:
                book['quantity'] = str(int(book['quantity']) - 1)
                save_books.save_books(books)
                print("Book lent successfully")
                return
            else:
                print("Book is out of stock")
                return
    print("Book not found")