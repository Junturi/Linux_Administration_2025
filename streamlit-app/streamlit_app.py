import streamlit as st

st.set_page_config(
    page_title="Data-analysis"
)

st.write("# Tervetuloa Data-analysis -sivulleni!")

st.sidebar.success("Valitse näytettävä data yläpuolelta.")

st.markdown(
    """
    Tälle sivulle on koottu eri viikkotehtäviin liittyvät Streamlit-sovellukset. Löydät kaikki sovellukset vasemmasta sivupalkista.

    Viikon 3 viikkotehtävää varten tein Streamlit-sovelluksen Oulun Kaupungin tulostusmääristä.
    Datan hain [Open Data Portalista](https://www.opendata.fi/data/en_GB/dataset/tulostusmaarat-vuodesta-2019-lahtien), ja latasin sen CSV-tiedostosta tietokantaan.
    Streamlit-sovellus hakee datan tietokannasta ja näyttää pari kivaa käppyrää.

    Viikon 4 viikkotehtävässä haetaan säätietoja [OpenWeatherMapin](https://openweathermap.org/) API:sta.
    Säätiedot haetaan ajastetusti CRON-skriptin avulla 15 minuutin välein. Data lisätään tietokantaan.
    Streamlit-sovellus hakee datan tietokannasta.
    """
)
