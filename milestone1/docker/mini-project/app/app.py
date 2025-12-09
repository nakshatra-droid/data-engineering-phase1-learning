import psycopg2
import time

def connect_db():
    try:
        connection=connection = psycopg2.connect(
            host="db",        
            database="dockerdb",
            user="dockeruser",
            password="dockerpass"
        )
        print("Connected to PostgreSQL successfully.")
        return connection
    except Exception as e:
        print("Database connection failed:", e)
        return None
    
def insert_user(connection):
    cursor=connection.cursor()
    cursor.execute(""" INSERT INTO users (username,email) VALUES ('JohnDoe','john@example.com');""")
    connection.commit()
    cursor.close()
    print("Inserted a new user into DB.")

def get_users(connection):
    cursor=connection.cursor()
    cursor.execute("SELECT * FROM users;")
    rows=cursor.fetchall()
    cursor.close()
    return rows

if __name__ == "__main__":
    print("Waiting for DB to be ready...")
    time.sleep(10)
    
    conn=connect_db()
    if conn:
        insert_user(conn)
        users=get_users(conn)
        for user in users:
            print(user)
        conn.close()