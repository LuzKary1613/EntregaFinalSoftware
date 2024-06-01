import psycopg2

def test_connection():
    try:
        conn = psycopg2.connect(
            dbname="grocery_db",
            user="postgres",
            password="1234",
            host="localhost",
            port="5432",
            options="-c client_encoding=UTF8"
        )
        cur = conn.cursor()
        cur.execute("SELECT 1;")
        print("Connection successful")
        cur.close()
        conn.close()
    except Exception as e:
        print(f"Error connecting to the database: {e}")

if __name__ == '__main__':
    test_connection()

