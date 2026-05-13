import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="phonepe_db",
    user="postgres",
    password="newpassword123"
)

cursor = conn.cursor()
print("Connected to PostgreSQL")