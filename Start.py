import streamlit as st
import pandas as pd
from utils.data_manager import DataManager
from utils.login_manager import LoginManager

data_manager = DataManager(fs_protocol='webdav', fs_root_folder="Blutvolumenrechner")
login_manager = LoginManager(data_manager)
login_manager.login_register()

data_manager.load_user_data(
    session_state_key='data_df', 
    file_name='data.csv', 
    initial_value = pd.DataFrame(), 
    parse_dates = ['timestamp']
    )

st.title("Blutvolumenrechner")

st.write("Willkommen zum Blutvolumenrechner!")
st.write(" Hier können Sie Ihr Blutvolumen berechnen und über die Zeit verfolgen.")

st.write("Dieser Rechner verwendet die Nadlerformel, welche die Grösse, das Gewicht und das Geschlecht miteinbezieht um ein approximatives Blutvolumen zu berechnen. Dies kann nützlich sein, um abschätzen zu können, ob man Blutspenden darf oder nicht.")


st.write("Disclaimer: Viele Krankheiten und Gesundheitszustände können das Blutvolumen beeinflussen. Auch Sportler erreichen durch das Training oftmals ein höheres Blutvolumen. Der Rechner beachtet diese Änderungen nicht und soll demnach nur als Schätzung wahrgenommen werden!")

# !! WICHTIG: Eure Emails müssen in der App erscheinen!!

# Streamlit über den Text unten direkt in die App - cool!
"""
Diese App wurde von folgenden Personen entwickelt:
- Michelle Weder (wedermic@students.zhaw.ch)
- Lisa Pianezzi (pianelis@students.zhaw.ch)
"""

