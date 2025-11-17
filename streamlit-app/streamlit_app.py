import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

def get_data_from_db():
    query = "SELECT * FROM oulu;"
    engine = create_engine(f"mysql+mysqlconnector://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}")
    df = pd.read_sql(query, engine)

    return df

def main():
    st.title("Oulun kaupungin tulostusmäärät vuodesta 2019 lähtien")

    df = get_data_from_db()
    df.columns = df.columns.str.strip()

    # Plot total pages per year for all page types
    page_columns = [
        "Mustavalkosivu_A4",
        "Varisivu_A4",
        "Mustavalkosivu_A3",
        "Varisivu_A3",
    ]
    
    # Reshape to lon format
    df_long = pd.melt(
        df,
        id_vars=["Vuosi"],
        value_vars=page_columns,
        var_name="Tulostetyypit",
        value_name="Sivua"
    )

    # Plot all in one figure
    fig1 = px.bar(
        df_long,
        x="Vuosi",
        y="Sivua",
        color="Tulostetyypit",
        barmode="group",
        title="Tulosteita per vuosi"
    )
    st.plotly_chart(fig1, width='stretch')

    # Create a drop down selection
    toimialat = df["Toimiala"].unique()
    selected_toimiala = st.selectbox("Valitse toimiala nähdäksesi tulosteiden kokonaismäärän", toimialat)

    # Filter the data by selection
    df_filtered = df[df["Toimiala"] == selected_toimiala].copy()

    # Plot the selection
    fig2 = px.bar(
        df_filtered,
        x="Vuosi",
        y="Yhteensa",
        title=f"{selected_toimiala} tulosteet vuosittain"
    )
    st.plotly_chart(fig2, width='stretch')

    # Add source to the end
    st.markdown(
        "Data on haettu MySQL-tietokannasta. \n"
        "Alkuperäinen lähde: [Open Data Portal](https://www.opendata.fi/data/en_GB/dataset/tulostusmaarat-vuodesta-2019-lahtien)"
    )

if __name__ == "__main__":
    main()
