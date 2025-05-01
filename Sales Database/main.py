import psycopg2

# === Configuration ===
DB_NAME = 'your_db_name'
DB_USER = 'your_username'
DB_PASSWORD = 'your_password'
DB_HOST = 'localhost'  # or your host IP
DB_PORT = '5432'

def execute_sql_file(filename, conn):
    with open(filename, 'r') as file:
        sql = file.read()
    with conn.cursor() as cursor:
        cursor.execute(sql)
    conn.commit()

# === Main ===
def main():
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        print("Connected to the database.")

        print("Creating schema...")
        execute_sql_file('GeneratedScript.sql', conn)

        print("Inserting data...")
        execute_sql_file('CoffeeData.sql', conn)

        print("🎉 Done!")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        if conn:
            conn.close()
            print("Connection closed.")

if __name__ == '__main__':
    main()
