from flask import Flask, render_template
import mysql.connector, os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/')
def home():
    # Connect to MySQL, get the enviromental variables from .env
    conn = mysql.connector.connect (
        host="localhost",
        user=os.getenv("USERNAME"),
        password=os.getenv("PASSWORD"),
        database=os.getenv("DATABASE")
    )

    # Execute command
    cursor = conn.cursor()
    cursor.execute("SELECT CURRENT_TIMESTAMP;")
    result = cursor.fetchone()

    # Close connection
    cursor.close()
    conn.close()

    return render_template("index.html", time=result[0])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5000)