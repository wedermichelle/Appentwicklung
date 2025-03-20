from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py') 

import streamlit as st
import pandas as pd

st.title('Blutvolumen Werte')

if "data_df" not in st.session_state:
    st.session_state["data_df"] = pd.DataFrame(columns=["timestamp", "geschlecht", "gewicht", "groesse", "blutvolumen"])

data_df = st.session_state['data_df']
if data_df.empty:
    st.info('Keine Blutvolumen Daten vorhanden. Berechnen Sie Ihr Blutvolumen auf der Startseite.')
    st.stop()

if "timestamp" in data_df.columns:
    data_df["timestamp"] = pd.to_datetime(data_df["timestamp"], errors='coerce')
    data_df = data_df.sort_values("timestamp", ascending=False)

data_df.columns = ["Datum & Zeit", "Geschlecht", "Gewicht", "Größe", "Blutvolumen"]

st.dataframe(data_df)