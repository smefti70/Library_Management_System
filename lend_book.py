# import json
# from datetime import datetime, timedelta
# import save_books
#
# def lend_book(books, book_id):
#     for book in books:
#         if book['isbn'] == book_id:
#             if int(book['quantity']) > 0:
#                 borrower_name = input("Enter borrower's name: ")
#                 phone_number = input("Enter borrower's phone number: ")
#                 due_date = (datetime.now() + timedelta(days=14)).strftime("%d-%m-%Y")
#
#                 lending_info = {
#                     "borrower_name": borrower_name,
#                     "phone_number" : phone_number,
#                     "book_title" : book['title'],
#                     "isbn" : book_id,
#                     "due_date" : due_date
#                 }
#
#                 with open("lending_info.json", "r") as file:
#                     lending_records = json.load(file)
#
#                 lending_records.append(lending_info)
#
#                 with open("lending_info.json", "w") as file:
#                     json.dump(lending_records, file, indent=4)
#
#
#                 book['quantity'] = int(book['quantity']) - 1
#                 save_books.save_books(books)
#                 print(f"Book lent successfully to {borrower_name}. Return by {due_date}.")
#                 return
#             else:
#                 print("There are not enough books available to lend.")
#                 return
#     print("Book not found")

import json
from datetime import datetime, timedelta
import save_books

def lend_book(books, book_id):
    for book in books:
        if book['isbn'] == book_id:
            if int(book['quantity']) > 0:
                borrower_name = input("Enter borrower's name: ")
                phone_number = input("Enter borrower's phone number: ")
                due_date = (datetime.now() + timedelta(days=14)).strftime("%d-%m-%Y")

                lending_info = {
                    "borrower_name": borrower_name,
                    "phone_number" : phone_number,
                    "book_title" : book['title'],
                    "isbn" : book_id,
                    "due_date" : due_date
                }

                # Handle file reading safely, initializing it if it's empty or doesn't exist
                try:
                    with open("lending_info.json", "r") as file:
                        lending_records = json.load(file)
                except (FileNotFoundError, json.JSONDecodeError):
                    lending_records = []  # If file doesn't exist or is empty, initialize an empty list

                lending_records.append(lending_info)

                # Write the updated lending records back to the file
                with open("lending_info.json", "w") as file:
                    json.dump(lending_records, file, indent=4)

                # Decrease the book quantity
                book['quantity'] = int(book['quantity']) - 1
                save_books.save_books(books)
                print(f"Book lent successfully to {borrower_name}. Return by {due_date}.")
                return
            else:
                print("There are not enough books available to lend.")
                return
    print("Book not found")
