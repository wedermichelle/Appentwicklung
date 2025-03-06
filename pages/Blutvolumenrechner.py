import streamlit as st

st.title("Blutvolumenrechner")

st.write("Dieser Rechner berechnet das approximative Blutvolumen anhand der Nadler-Formel. Have fun:)")

st.write("Bitte geben Sie Ihr biologisches Geschlecht an:")

col1, col2 = st.columns(2)

geschlecht = None

with col1:
    if st.button ("Männlich"):
        st.session_state.geschlecht = "Männlich"


with col2:
    if st.button ("Weiblich"):
        st.session_state.geschlecht = "Weiblich"    

if st.session_state.geschlecht:
    st.write(f"Geschlecht: {geschlecht}")
    gewicht = st.number_input("Bitte geben Sie Ihr Gewicht in kg ein:", min_value=0.0, format="%.2f")
    groesse = st.number_input("Bitte geben Sie Ihre Größe in cm ein:", min_value=0.0, format="%.2f")

    if gewicht > 0 and groesse > 0:
        if st.session_state.geschlecht == "Männlich":
            blutvolumen = 0.3669 * (groesse / 100) ** 3 + 0.03219 * gewicht + 0.6041
        else:
            blutvolumen = 0.3561 * (groesse / 100) ** 3 + 0.03308 * gewicht + 0.1833

        st.write(f"Ihr approximatives Blutvolumen beträgt: {blutvolumen:.2f} Liter")

