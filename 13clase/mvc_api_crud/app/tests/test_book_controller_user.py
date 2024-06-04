def test_get_books_user(test_client, user_auth_headers):
    response = test_client.get("/api/books", headers=user_auth_headers)
    assert response.status_code == 200
    assert response.json == []


def test_create_book(test_client, auth_headers):
    data = {"title":"ejemplo", "author":"ejemplo", "edition":"ejemplo", "availability":"ejemplo"}
    response = test_client.post("/api/books", json=data, headers=auth_headers)
    assert response.status_code == 201
    assert response.json["title"] == "ejemplo"


def test_get_book_user(test_client, user_auth_headers):
    # Ahora obtén el libro
    response = test_client.get(f"/api/books/1", headers=user_auth_headers)
    assert response.status_code == 200
    assert "title" in response.json

def test_create_book_user(test_client, user_auth_headers):
    data = {"title":"ejemplo", "author":"ejemplo", "edition":"ejemplo", "availability":"ejemplo"}
    response = test_client.post("/api/books", json=data, headers=user_auth_headers)
    assert response.status_code == 403


def test_update_book_user(test_client, user_auth_headers):
    # Ahora actualiza el libro
    update_data = {"title":"ejemplo", "author":"ejemploUP", "edition":"ejemploUP", "availability":"ejemplo"}
    response = test_client.put("/api/books/1", json=update_data, headers=user_auth_headers)
    assert response.status_code == 403


def test_delete_book_user(test_client, user_auth_headers):
    # Ahora elimina el libro
    response = test_client.delete("/api/books/1", headers=user_auth_headers)
    assert response.status_code == 403
