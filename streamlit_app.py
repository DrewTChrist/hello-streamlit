import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import requests

EX = "https://api.torn.com/user/:ID?selections=:SELECTIONS&key=:KEY"
BASE = "https://api.torn.com"
USER = BASE + "/user/"
PROPERTY = BASE + "/property/"
FACTION = BASE + "/faction/"
COMPANY = BASE + "/company/"
MARKET = BASE + "/market/"
TORN = BASE + "/torn/"

with st.form("data_form"):
    key = st.text_input("API Key", placeholder="Enter your API key")
    id = st.text_input("ID", placeholder="Enter an ID")
    selections = st.selections("Selections", placeholder="Enter selections")
    result = requests.get(USER + id + "&selections=" + selections + "&key=" + key)
    st.write(result.text)



# num_points = st.slider("Number of points in spiral", 1, 10000, 1100)
# num_turns = st.slider("Number of turns in spiral", 1, 300, 31)
# indices = np.linspace(0, 1, num_points)
# theta = 2 * np.pi * num_turns * indices
# radius = indices
# x = radius * np.cos(theta)
# y = radius * np.sin(theta)
# df = pd.DataFrame({
#     "x": x,
#     "y": y,
#     "idx": indices,
#     "rand": np.random.randn(num_points),
# })
# st.altair_chart(alt.Chart(df, height=700, width=700)
#     .mark_point(filled=True)
#     .encode(
#         x=alt.X("x", axis=None),
#         y=alt.Y("y", axis=None),
#         color=alt.Color("idx", legend=None, scale=alt.Scale()),
#         size=alt.Size("rand", legend=None, scale=alt.Scale(range=[1, 150])),
#     ))
