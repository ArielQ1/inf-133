from database import db


class Book(db.Model):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    edition = db.Column(db.String(100), nullable=False)
    availability = db.Column(db.String(100), nullable=False)

    def __init__(self, title, author, edition, availability):
        self.title = title
        self.author = author
        self.edition = edition
        self.availability = availability

    # Guarda un animal en la base de datos
    def save(self):
        db.session.add(self)
        db.session.commit()

    # Obtiene todos los animales de la base de datos
    @staticmethod
    def get_all():
        return Book.query.all()

    # Obtiene un animal por su ID
    @staticmethod
    def get_by_id(id):
        return Book.query.get(id)
    
    # Actualiza un animal en la base de datos
    def update(self, title=None, author=None, edition=None, availability=None):
        if title is not None:
            self.title = title
        if author is not None:
            self.author = author
        if edition is not None:
            self.edition = edition
        if availability is not None:
            self.availability = availability
        db.session.commit()

    # Elimina un animal de la base de datos
    def delete(self):
        db.session.delete(self)
        db.session.commit()
