import save_books
def return_book(books, book_id):
    for book in books:
        if book['isbn'] == str(book_id):
            book['quantity'] = str(int(book['quantity']) + 1)
            save_books.save_books(books)
            print("Book returned successfully")
            return