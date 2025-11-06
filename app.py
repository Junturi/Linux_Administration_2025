from flask import FLask
import mysql.connector
import os

load_dotenv()

app = Flask(__name__)

@app.rout('/')
def home():
    # Connect to MySQL
    conn = mysql.connector.connect (
        host = "localhost",
        user = "USERNAME",
        password = "PASSWORD",
        database = "DATABASE"
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