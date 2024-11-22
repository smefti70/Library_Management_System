import save_books
def delete_book(books, book_id):
    for book in books:
        if book['isbn'] == str(book_id):
            books.remove(book)
            save_books.save_books(books)
            print("Book deleted successfully")
            return
    print("Book not found")