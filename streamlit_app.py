import streamlit as st

login_page = st.Page("login.py", title="Login", default=True)
edit_price_list = st.Page("edit_price_list.py", title="Edit Price List")
view_price_list = st.Page("view_price_list.py", title="View Price List")
admin_page = st.Page("admin.py", title="Administration", default=True)

state_defaults = [
    {"api_key": ""}, 
    {"profile": None},
    {'admins': [3308015]}
]

# Add state defaults to session state
# Looks hacky, but you must check if the value already exists
_ = [
    [
        st.session_state.update({k: v})
        for (k, v) in item.items()
        if k not in st.session_state
    ]
    for item in state_defaults
]

# st.write(st.session_state)

# st.write(st.query_params)

if st.session_state.profile:
    if st.session_state.profile["player_id"] in st.session_state["admins"]:
        nav = st.navigation([admin_page, edit_price_list])
    else:
        nav = st.navigation([edit_price_list])
elif "userid" in st.query_params:
    nav = st.navigation([view_price_list])
else:
    nav = st.navigation([login_page])

nav.run()