import sqlite3

conn = sqlite3.connect("restaurante.db")
try:
    conn.execute(
        """
        CREATE TABLE PLATOS
        (id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        precio REAL NOT NULL,
        categoria TEXT NOT NULL);
        """
    )
except sqlite3.OperationalError:
    print("La tabla Platos ya existe")
try:
    conn.execute(
        """
        CREATE TABLE MESAS
        (id INTEGER PRIMARY KEY,
        numero INTEGER NOT NULL);
        """
    )
except sqlite3.OperationalError:
    print("La tabla Mesas ya existe")
    
try:
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
except sqlite3.OperationalError:
    print("La tabla Pedidos ya existe")

# Insertar datos de platos
conn.execute(
    """
    INSERT INTO PLATOS (nombre, precio, categoria) 
    VALUES ('PIZZA', 10.99, 'Italiana'), ('HAMBURGUESA', 8.99, 'Americana'), 
            ('SUCHI', 12.99, 'Japonesa'),('ENSALADA', 10.99, 'Vegetariana')
    """
)

# Insertar datos de mesas 
conn.execute(
    """
    INSERT INTO MESAS (numero) 
    VALUES (1),(2),(3),(4)
    """
)
#Insertar datos Pedidos
conn.execute(
    """
    INSERT INTO PEDIDOS (plato_id, mesa_id, cantidad, fecha) 
    VALUES 
    (1, 2, 2, '2024-04-01'),
    (2, 3, 1, '2024-04-01'),
    (3, 1, 3, '2024-04-02'),
    (4, 4, 1, '2024-04-02')
    """
)

# Consultar datos
print("\nPlatos:")
cursor = conn.execute("SELECT * FROM PLATOS")
for row in cursor:
    print(row)
# Consultar datos
print("\nMesas:")
cursor = conn.execute("SELECT * FROM MESAS")
for row in cursor:
    print(row)
#Consultar datos 
print("\nPedidos")
cursor = conn.execute("SELECT * FROM PEDIDOS")
for row in cursor:
    print(row)

# Actualizar el precio del plato id 2
conn.execute(
    """
    UPDATE PLATOS
    SET precio = 9.99
    WHERE id = 2
    """
)
#Cambia la categoria del plato con id 3
conn.execute(
    """
    UPDATE PLATOS
    SET categoria = 'Fusión'
    WHERE id = 3
    """
)
#Elimina el plato con id 4 
#conn.execute(
#    """
#    DELETE FROM PLATOS
#    WHERE id = 4
#    """
#)
#Elimina el pedido con id 3
conn.execute(
    """
    DELETE FROM PEDIDOS
    WHERE id = 3
    """
)

# Consultar datos
print("\nPlatos:")
cursor = conn.execute("SELECT * FROM PLATOS")
for row in cursor:
    print(row)
    
print("\nPedidos")
cursor = conn.execute("SELECT * FROM PEDIDOS")
for row in cursor:
    print(row)





#Guarda Informacion
conn.commit()
# Cerrar conexión
conn.close()