import save_books
import json

def return_book(books, book_id, borrower_name):
    # Ensure book_id is an integer for comparison
    book_id = int(book_id)

    # Read the lending record using json.load() to parse the entire file properly
    try:
        with open("lending_info.json", "r") as file:
            lending_records = json.load(file)  # Directly load JSON
    except FileNotFoundError:
        print("Lending information file not found.")
        return
    except json.JSONDecodeError:
        print("Error decoding the JSON in lending_info.json.")
        return

    updated_records = []
    is_returned = False
    book_found = False

    for lending_info in lending_records:

        # Ensure both the lending_info['isbn'] and book_id are compared as integers
        if int(lending_info['isbn']) == book_id:  # Compare both as integers
            book_found = True
            if lending_info['borrower_name'].lower() == borrower_name.lower():  # Match by borrower name
                is_returned = True
                print(f"Book titled '{lending_info['book_title']}' returned by {lending_info['borrower_name']}.")
            else:
                updated_records.append(lending_info)
        else:
            updated_records.append(lending_info)

    if book_found:
        if is_returned:
            # Save updated lending records (remove the returned book's record)
            with open("lending_info.json", "w") as file:
                json.dump(updated_records, file, indent=4)

            # Update book quantity and save
            for book in books:
                if int(book['isbn']) == book_id:
                    book['quantity'] = int(book['quantity']) + 1
                    save_books.save_books(books)
                    break
        else:
            print(f"No record of this book being lent to {borrower_name}.")
    else:
        print(f"Book with ISBN {book_id} not found.")
