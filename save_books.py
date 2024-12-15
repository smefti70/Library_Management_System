import json
def save_books(book_list):
    with open("books.json", "w") as file:
        json.dump(book_list,file,indent=4)