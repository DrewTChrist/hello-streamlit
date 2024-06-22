import streamlit as st

st.title("Edit Your Price List")

tab1, tab2, tab3, tab4 = st.tabs(["Plushies", "Flowers", "Boosters", "Meds"])
# special, drugs, enhancers, candy, alcohol, special
# supply packs, artifacts, collectibles

with tab1:
    st.header("Plushies")
    st.dataframe({"plushies": ["jaguar", "wolverine"]})

with tab2:
    st.header("Flowers")
    st.dataframe()

with tab3:
    st.header("Boosters")
    st.dataframe()

with tab4:
    st.header("Meds")
    st.dataframe()