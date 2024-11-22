def save_books(book_list):
    with open("books.csv", "w") as f:
        for book in book_list:
            f.write(f"{book['title']},{book['author']},{book['isbn']},{book['year']},{book['price']},{book['quantity']}\n")