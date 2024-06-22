import streamlit as st
import requests
import json
import dal

st.title("Torn Price List")

st.header("Login")

api_key = st.text_input(
    "API Key", 
    type="password",
    value=st.session_state.api_key
)

st.caption("You can generate a limited access API key in your Torn account settings")

submit = st.button(
    "Login",
    type="primary"
)

INVALID_API_KEY = {"error":{"code":2,"error":"Incorrect key"}}

if submit:
    if api_key != "":    
        url = "https://api.torn.com/user/?selections=profile&key=" + api_key
        response = requests.get(url)
        resp_json = json.loads(response.text)
        if resp_json == INVALID_API_KEY:
            st.error("Error: Invalid API Key")
        else:
            st.session_state.api_key = api_key
            st.session_state.profile = resp_json
            try:
                user_id = dal.create_user(
                    st.secrets["DB_STRING"],
                    st.session_state.profile["name"],
                    st.session_state.profile["player_id"],
                    st.session_state["api_key"]
                )
                dal.create_settings(st.secrets["DB_STRING"], user_id)
                # update api key here?
            except dal.UniqueViolation:
                pass
            st.rerun()
    else:
        st.error("Error: API Key is empty")