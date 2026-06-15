import streamlit as st

st.set_page_config(
    page_title="Friday Night at the ER",
    page_icon="🏥",
    layout="wide"
)

GAME_LOGO = "1548433148198.png"
COMPANY_LOGO = "PHI-Air-Med_logo-2023.jpg"

st.markdown("""
<style>
.stApp {
    background-color: #0f0f0f;
    color: white;
}

.hero {
    background: linear-gradient(135deg, #000000, #2b2b2b);
    padding: 40px;
    border-radius: 20px;
    border: 3px solid #f5c400;
    text-align: center;
}

.card {
    background-color: #1c1c1c;
    padding: 25px;
    border-radius: 16px;
    border-left: 6px solid #f5c400;
    color: white;
    box-shadow: 0 4px 15px rgba(245,196,0,0.25);
}

h1, h2, h3 {
    color: #f5c400;
}

div.stButton > button {
    background-color: #f5c400;
    color: black;
    font-weight: bold;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)
