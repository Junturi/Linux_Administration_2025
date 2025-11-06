from flask import Flask
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/')
def home():
    # Connect to MySQL
    conn = mysql.connector.connect (
        host="localhost",
        user=os.getenv("USERNAME"),
        password=os.getenv("PASSWORD"),
        database=os.getenv("DATABASE")
    )

    # Execute command
    cursor = conn.cursor()
    cursor.execute("SELECT 'Hello from MySQL!'")
    result = cursor.fetchone()

    # Close connection
    cursor.close()
    conn.close()

    return f"<h1>{result[0]}</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5000)