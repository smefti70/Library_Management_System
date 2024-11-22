def load_books(file_path="books.csv"):
    books = []
    with open(file_path, "r") as file:
        for line in file:
            title, author, isbn, year, price, quantity = line.strip().split(",")
            books.append({
                "title": title,
                "author": author,
                "isbn": isbn,
                "year": year,
                "price": price,
                "quantity": quantity
            })
    return books