import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import requests
import json

EX = "https://api.torn.com/user/:ID?selections=:SELECTIONS&key=:KEY"
BASE = "https://api.torn.com"
USER = "/user/"
PROPERTY = "/property/"
FACTION = "/faction/"
COMPANY = "/company/"
MARKET = "/market/"
TORN = "/torn/"

# {"error":{"code":2,"error":"Incorrect key"}}
# {"error": {"code": 7,"error": "Incorrect ID-entity relation"}}
# {"error": {"code": 6,"error": "Incorrect ID"}}
# 
# https://api.torn.com/user/?selections=lookup&key=V8fGQQScGJ4HnEjE


def update_selections(section, key):
    selections = []
    if section != "" and key != "":
        response = requests.get(BASE + section + "?selections=lookup" + "&key=" + key)
        obj = json.loads(response.text)
        selections = obj['selections']
    return selections


# key = st.text_input("API Key", placeholder="Enter your API key")
key = st.session_state.api_key
section = st.selectbox(
    "Area", 
    options=[USER, PROPERTY, FACTION, COMPANY, MARKET, TORN],
)
selections = st.multiselect(
    "Selections", 
    placeholder="Enter selections",
    options=update_selections(section, key)
)

with st.form("data_form"):
    id = st.text_input("ID", placeholder="Enter an ID")
    if key != "" and selections != "":
        api_url = BASE + section + id + "?selections=" + ''.join([f"{item}," for item in selections]).rstrip(',') + "&key=" + key
        result = requests.get(api_url)
        obj = json.loads(result.text)
        st.write(obj)
    st.form_submit_button("Get data")
