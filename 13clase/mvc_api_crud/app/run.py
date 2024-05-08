from flask import Flask
from controllers.book_controller import book_bp
from database import db

app = Flask(__name__)

#Configuracion de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Inicializa la base de datos
db.init_app(app)

#Registra el blueprint de libros en la aplicaion
app.register_blueprint(book_bp, url_prefix="/api")

#Crea las tablas si no existen
with app.app_context():
    #Crea las tablas
    db.create_all()

#Ejecuta la aplicacion
if __name__ == "__main__":
    app.run(debug=True)