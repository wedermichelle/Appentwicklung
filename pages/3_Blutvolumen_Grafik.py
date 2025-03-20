from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py')  


import streamlit as st

st.title('Blutvolumen Verlauf')

data_df = st.session_state['data_df']
if data_df.empty:
    st.info('Keine Blutvolumen Daten vorhanden. Berechnen Sie Ihren Blutvolumen auf der Startseite.')
    st.stop()

st.caption('Gewicht über Zeit (kg)')
st.line_chart(data=data_df.set_index('timestamp')['gewicht'], 
                use_container_width=True)

st.caption('Grösse über Zeit (m)')
st.line_chart(data=data_df.set_index('timestamp')['groesse'],
                use_container_width=True)

st.caption('Blutvolumen über Zeit (L)')
st.line_chart(data=data_df.set_index('timestamp')['blutvolumen'],
                use_container_width=True)
