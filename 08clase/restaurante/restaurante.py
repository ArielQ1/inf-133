import sqlite3

conn = sqlite3.connect("restaurante.db")

conn.execute(
    """
    CREATE TABLE PLATOS
    (id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    precio REAL NOT NULL,
    categoria TEXT NOT NULL);
    """
)

conn.execute(
    """
    CREATE TABLE MESAS
    (id INTEGER PRIMARY KEY,
    numero INTEGER NOT NULL);
    """
)

conn.execute(
    """
    CREATE TABLE PEDIDOS
    (id INTEGER PRIMARY KEY,
    plato_id INTEGER NOT NULL,
    mesa_id INTEGER NOT NULL,
    cantidad INTEGER NOT NULL,
    fecha DATE NOT NULL,
    FOREIGN KEY (plato_id) REFERENCES PLATOS(id),
    FOREIGN KEY (mesa_id) REFERENCES MESAS(id));
    """
)














# Insertar datos de platos
conn.execute(
    """
    INSERT INTO PLATOS (nombre, precio, categoria) 
    VALUES ('PIZZA', 10.99, 'Italiana')
    """
)
conn.execute(
    """
    INSERT INTO PLATOS (nombre, precio, categoria) 
    VALUES ('HAMBURGUESA', 8.99, 'Americana')
    """
)
conn.execute(
    """
    INSERT INTO PLATOS (nombre, precio, categoria) 
    VALUES ('SUCHI', 12.99, 'Japonesa')
    """
)
conn.execute(
    """
    INSERT INTO PLATOS (nombre, precio, categoria) 
    VALUES ('ENSALADA', 10.99, 'Vegetariana')
    """
)
# Insertar datos de mesas 
conn.execute(
    """
    INSERT INTO MESAS (numero) 
    VALUES (1)
    """
)
conn.execute(
    """
    INSERT INTO MESAS (numero) 
    VALUES (2)
    """
)
conn.execute(
    """
    INSERT INTO MESAS (numero) 
    VALUES (3)
    """
)
conn.execute(
    """
    INSERT INTO MESAS (numero) 
    VALUES (4)
    """
)

# Consultar datos
#print("PLATOS:")
#cursor = conn.execute("SELECT * FROM PLATOS")
#for row in cursor:
#    print(row)








# Cerrar conexión
conn.close()