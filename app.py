import streamlit as st

st.set_page_config(page_title="Friday Night at the ER", layout="wide")

st.title("🏥 Friday Night at the ER")
st.subheader("Team Performance Dashboard")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric("Team A", "0", "Quality")
    st.metric("Cost", "$0")

with col2:
    st.metric("Team B", "0", "Quality")
    st.metric("Cost", "$0")

with col3:
    st.metric("Team C", "0", "Quality")
    st.metric("Cost", "$0")

with col4:
    st.metric("Team D", "0", "Quality")
    st.metric("Cost", "$0")

with col5:
    st.metric("Team E", "0", "Quality")
    st.metric("Cost", "$0")

st.divider()

st.header("Results")

st.info("Prototype dashboard successfully deployed.")
