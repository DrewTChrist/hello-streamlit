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


# [x] show drugs taken ecstasy, xanax, etc
# [] candy used
# [x] show online time
# [x] show donator status/days
# [x] show property
# [] show merits bought and points used or refills done
# [] books read, boosters used
# [x] ELO
# [x] job and job points used, important if military


key = st.session_state.api_key
selections = "basic,profile,personalstats"

with st.form("data_form"):
    id = st.text_input("User ID", placeholder="User ID")
    if key != "":
        api_url = BASE + USER + id + "?selections=" + selections + "&key=" + key
        result = requests.get(api_url)
        obj = json.loads(result.text)
        df = pd.DataFrame({
            "Property1": [
                "Name", 
                "User ID", 
                "Level",
                "Age",
                "Online Time", 
                "Donator Status", 
                "Donator Days", 
                "ELO", 
                "Job", 
                "Job Points Used", 
                "Property", 
                "", 
            ],
            "Values1": [
                obj["name"], 
                obj["player_id"], 
                obj["level"],
                obj["age"],
                obj["personalstats"]["useractivity"], 
                obj["donator"], 
                obj["personalstats"]["daysbeendonator"], 
                obj["personalstats"]["elo"], 
                obj["job"]["job"], 
                obj["personalstats"]["jobpointsused"], 
                obj["property"], 
                "", 
            ],
            "Property2": [
                "Drugs Used",
                "Overdoses",
                "Cannabis", 
                "Ecstasy", 
                "Ketamine", 
                "LSD", 
                "Opium", 
                "Shrooms", 
                "Speed", 
                "PCP", 
                "Xanax", 
                "Vicodin",
            ],
            "Values2": [
                obj["personalstats"]["drugsused"],
                obj["personalstats"]["overdosed"],
                obj["personalstats"]["cantaken"],
                obj["personalstats"]["exttaken"],
                obj["personalstats"]["kettaken"],
                obj["personalstats"]["lsdtaken"],
                obj["personalstats"]["opitaken"],
                obj["personalstats"]["shrtaken"],
                obj["personalstats"]["spetaken"],
                obj["personalstats"]["pcptaken"],
                obj["personalstats"]["xantaken"],
                obj["personalstats"]["victaken"]
            ],
            "Property3": [0,0,0,0,0,0,0,0,0,0,0,0],
            "Values3": [0,0,0,0,0,0,0,0,0,0,0,0]
        })
        st.dataframe(
            df,
            column_config={
                "Property1": "Property",
                "Values1": "Value",
                "Property2": "Property",
                "Values2": "Values",
                "Property3": "Property",
                "Values3": "Values"
            },
            hide_index=True
        )
        # st.write(obj)
    st.form_submit_button("Get data")