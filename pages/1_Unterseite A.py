import streamlit as st

st.title("Blutvolumenrechner")

st.write("Dieser Rechner berechnet das approximative Blutvolumen anhand der Nadler-Formel. Have fun:)")

st.write("Bitte geben Sie Ihr biologisches Geschlecht an:")
col1, col2 = st.columns(2)

with col1:
    if st.button ("Männlich"):
        st.write("code here")

with col2:
    if st.button ("Weiblich"):
        st.write("code here")

