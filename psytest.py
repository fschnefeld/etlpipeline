import psycopg2

try:
    connection = psycopg2.connect(
        dbname="coloplast",
        user="postgres",
        password="WXnqNB9bqMEC",
        host="localhost",
        port="5432"
    )
    print("Connection successful")
except Exception as e:
    print(f"Connection failed: {e}")