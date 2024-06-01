import psycopg2

# Función para probar la conexión a la base de datos
def test_connection():
    try:
        # Establece la conexión con la base de datos PostgreSQL
        conn = psycopg2.connect(
            dbname="grocery_db",
            user="postgres",
            password="1234",
            host="localhost",
            port="5432",
            options="-c client_encoding=UTF8"
        )
        cur = conn.cursor()  # Crea un cursor para ejecutar consultas
        cur.execute("SELECT 1;")  # Ejecuta una consulta simple para probar la conexión
        print("Connection successful")  # Imprime un mensaje si la conexión es exitosa
        cur.close()  # Cierra el cursor
        conn.close()  # Cierra la conexión
    except Exception as e:
        # Maneja cualquier excepción que ocurra y muestra un mensaje de error
        print(f"Error connecting to the database: {e}")

# Ejecuta la función de prueba de conexión si el script se ejecuta directamente
if __name__ == '__main__':
    test_connection()
