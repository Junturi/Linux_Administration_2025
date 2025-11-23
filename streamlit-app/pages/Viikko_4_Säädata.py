import streamlit as st
import mysql.connector
import pandas as pd
import os
from dotenv import load_dotenv

conn = mysql.connector.connect(
    host=os.getenv('DB_HOST'),
    user = os.getenv('DB_USER'),
    password = os.getenv('DB_PASSWORD'),
    database = os.getenv('DB_NAME2')
    )

df = pd.read_sql('SELECT * FROM weather_data ORDER BY timestamp DESC LIMIT 50', conn)

conn.close()

st.title("Sää Helsingissä")

st.header('Lämpötila viimeisen 12 tunnin aikana')
st.line_chart(
    df,
    x = "timestamp",
    y = "temperature",
    x_label = "Aika",
    y_label = "Lämpötila"
    )

st.header('Viimeiset 50 säähavaintoa')
st.dataframe(df)

st.markdown(
        "Data on haettu MySQL-tietokannasta. \n"
        "Alkuperäinen lähde: [OpenWeatherMap](https://openweathermap.org/)"
    )