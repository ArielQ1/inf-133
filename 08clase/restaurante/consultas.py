# Importar módulo sqlite3
import sqlite3
# Crear conexión a la base de datos
conn = sqlite3.connect("restaurante.db")

conn.execute(
    """
    INSERT INTO PLATOS (nombre, precio, categoria) 
    VALUES ('HOLANDESA', 1.99, 'Japonesa')
    """
)


# Consultar datos de PEDIDOS INNER JOIN
print("\nPEDIDOS: INNER JOIN")
cursor = conn.execute(
    """
    SELECT PEDIDOS.id, PLATOS.nombre, MESAS.numero 
    FROM PEDIDOS
    JOIN PLATOS ON PLATOS.id = PEDIDOS.plato_id 
    JOIN MESAS ON MESAS.id  = PEDIDOS.mesa_id
    """
)
for row in cursor:
    print(row)

# Consultar datos de matriculación LEFT JOIN
print("\nPEDIDOS LEFT JOIN:")
cursor = conn.execute(
    """
    SELECT P.*, PEDIDOS.id
    FROM PLATOS as P
    LEFT JOIN PEDIDOS ON P.id = PEDIDOS.plato_id
    """
)
for row in cursor:
    print(row)

    
#Guarda Informacion
conn.commit()
# Cerrar conexión
conn.close()