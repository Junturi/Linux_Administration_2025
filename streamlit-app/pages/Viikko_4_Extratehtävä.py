import streamlit as st
import requests

def show_kitty():
    image = requests.get("https://cataas.com/cat").content
    st.image(image)

st.button("Anna minulle kissa!", on_click=show_kitty)

st.markdown(
        "Kissat tarjoaa [CATAAS](https://cataas.com/)"
    )