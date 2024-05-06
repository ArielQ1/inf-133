def render_book_list(books):
    return[
        {
            "title": book.title,
            "author": book.author,
            "edition": book.edition,
            "availability":book.availability,
        }
        for book in books
    ]

def render_book_details(book):
    return {
        "id": book.id,
        "title": book.title,
        "author": book.author,
        "edition": book.edition,
        "availability":book.availability,
    }