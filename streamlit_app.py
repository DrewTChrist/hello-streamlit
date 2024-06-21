import streamlit as st

st.page_link("streamlit_app.py", label="Home", icon="🏠")
#st.page_link("pages/api.py", label="API", icon="1️⃣")
#st.page_link("pages/sniffer.py", label="Sniffer")

if "api_key" not in st.session_state:
    st.session_state.api_key = ""

api_key = st.text_input(
    "API Key", 
    type="password",
    value=st.session_state.api_key
)

login = st.button(
    "Login"
)

st.session_state.api_key = api_key