def view_books():
    print("Here are the books in the library:")
    print(
        f"{'Title':<15}{'Author':<15}{'ISBN':<10}{'Published':<12}{'Price':<8}{'Quantity':<10}"
    )
    print(
        f"{'-----':<15}{'------':<15}{'----':<10}{'---------':<12}{'-----':<8}{'-------':<10}"
    )
    with open("books.csv", "r") as f:
        for line in f:
            book_details = line.strip().split(",")
            # Format each field with a fixed width
            print(
                f"{book_details[0]:<15}{book_details[1]:<15}{book_details[2]:<10}{book_details[3]:<12}{book_details[4]:<8}{book_details[5]:<10}"
            )

