from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py')
import streamlit as st
from PIL import Image, ImageDraw
import os 

image_path = os.path.join(os.path.dirname(__file__), "milchkarton.png")

st.title("Blutvolumenrechner")

st.write("Dieser Rechner berechnet das approximative Blutvolumen anhand der Nadler-Formel. Have fun:)")

st.write("Bitte geben Sie Ihr biologisches Geschlecht an:")
col1, col2 = st.columns(2)

if "geschlecht" not in st.session_state:
    st.session_state.geschlecht = None

with col1:
    if st.button("Männlich"):
        st.session_state.geschlecht = "Männlich"

with col2:
    if st.button("Weiblich"):
        st.session_state.geschlecht = "Weiblich"

if st.session_state.geschlecht:
    geschlecht = st.session_state.geschlecht
    st.write(f"Geschlecht: {geschlecht}")
    gewicht = st.number_input("Bitte geben Sie Ihr Gewicht in kg ein:", min_value=0.0, format="%.2f")
    groesse = st.number_input("Bitte geben Sie Ihre Größe in cm ein:", min_value=0.0, format="%.2f")

    if gewicht > 0 and groesse > 0:
        if geschlecht == "Männlich":
            blutvolumen = 0.3669 * (groesse / 100) ** 3 + 0.03219 * gewicht + 0.6041
        else:
            blutvolumen = 0.3561 * (groesse / 100) ** 3 + 0.03308 * gewicht + 0.1833
        

        st.write(f"Ihr approximatives Blutvolumen beträgt: {blutvolumen:.2f} Liter")
        st.write(f"Dies entspricht so vielen Milchkartons:")

        try:
            image_path = os.path.join(os.path.dirname(__file__), "milchkarton.png")
            milk_carton_image = Image.open(image_path)
        except FileNotFoundError:
            st.error("Das Bild 'milchkarton.png' wurde nicht gefunden. Bitte stellen Sie sicher, dass es im gleichen Verzeichnis wie das Skript gespeichert ist.")
            st.stop()
        except Exception as e:
            st.error(f"Ein Fehler ist beim Laden des Bildes aufgetreten: {e}")
            st.stop()


        total_width = milk_carton_image.width * int(blutvolumen) + int(milk_carton_image.width * (blutvolumen - int(blutvolumen)))
        result_image = Image.new("RGBA", (total_width, milk_carton_image.height))


        for i in range(int(blutvolumen)):
            result_image.paste(milk_carton_image, (i * milk_carton_image.width, 0))

    
        partial_volume = blutvolumen - int(blutvolumen)
        if partial_volume > 0:
            partial_carton = milk_carton_image.crop((0, 0, int(milk_carton_image.width * partial_volume), milk_carton_image.height))
            result_image.paste(partial_carton, (int(blutvolumen) * milk_carton_image.width, 0))

        st.image(result_image, caption="Blutvolumen in Milchkartons")