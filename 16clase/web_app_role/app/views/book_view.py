from flask import render_template
from flask_login import current_user


# La función `list_animals` recibe una lista de
# animales y renderiza el template `animales.html`
def list_books(books):
    return render_template(
        "books.html",
        books=books,
        title="Lista de Libros",
        current_user=current_user,
    )


# La función `create_animal` renderiza el
# template `create_animal.html` o devuelve un JSON
# según la solicitud
def create_book():
    return render_template(
        "create_book.html", title="Crear Libro", current_user=current_user
    )


# La función `update_animal` recibe un animal
# y renderiza el template `update_animal.html`
def update_book(book):
    return render_template(
        "update_book.html",
        title="Editar Libro",
        book=book,
        current_user=current_user,
    )
