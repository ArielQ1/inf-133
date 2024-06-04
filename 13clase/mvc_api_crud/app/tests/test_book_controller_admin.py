def test_get_books(test_client, auth_headers):
    response = test_client.get("/api/books", headers=auth_headers)
    assert response.status_code == 200
    assert response.json == []


def test_create_book(test_client, auth_headers):
    data = {"title":"ejemplo", "author":"ejemplo", "edition":"ejemplo", "availability":"ejemplo"}
    response = test_client.post("/api/books", json=data, headers=auth_headers)
    assert response.status_code == 201
    assert response.json["title"] == "ejemplo"


def test_get_book(test_client, auth_headers):
    # Primero crea un libro
    data = {"title":"ejemplo", "author":"ejemplo", "edition":"ejemplo", "availability":"ejemplo"}
    response = test_client.post("/api/books", json=data, headers=auth_headers)
    assert response.status_code == 201
    book_id = response.json["id"]

    # Ahora obtén el libro
    response = test_client.get(f"/api/books/{book_id}", headers=auth_headers)
    assert response.status_code == 200
    assert response.json["title"] == "ejemplo"


def test_update_book(test_client, auth_headers):
    # Primero crea un libro
    data = {"title":"ejemplo", "author":"ejemplo", "edition":"ejemplo", "availability":"ejemplo"}
    response = test_client.post("/api/books", json=data, headers=auth_headers)
    assert response.status_code == 201
    book_id = response.json["id"]

    # Ahora actualiza el libro
    update_data = {"title":"ejemplo", "author":"ejemploUP", "edition":"ejemploUP", "availability":"ejemplo"}
    response = test_client.put(
        f"/api/books/{book_id}", json=update_data, headers=auth_headers
    )
    assert response.status_code == 200
    assert response.json["author"] == "ejemploUP"
    assert response.json["edition"] == "ejemploUP"


def test_delete_book(test_client, auth_headers):
    # Primero crea un libro
    data = {"title":"delete", "author":"delete", "edition":"delete", "availability":"delete"}
    response = test_client.post("/api/books", json=data, headers=auth_headers)
    assert response.status_code == 201
    book_id = response.json["id"]

    # Ahora elimina el libro
    response = test_client.delete(f"/api/books/{book_id}", headers=auth_headers)
    assert response.status_code == 204

    # Verifica que el libro ha sido eliminado
    response = test_client.get(f"/api/books/{book_id}", headers=auth_headers)
    assert response.status_code == 404

