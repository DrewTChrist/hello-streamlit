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
