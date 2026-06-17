import streamlit as st
import time

st.set_page_config(
    page_title="Friday Night at the ER",
    page_icon="🏥",
    layout="wide"
)

GAME_LOGO = "1548433148198.png"
COMPANY_LOGO = "PHI-Air-Med_logo-2023.jpg"

if "splash_done" not in st.session_state:
    st.session_state.splash_done = False

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #000000 0%, #1c1c1c 60%, #ffffff 100%);
    color: white;
}

.block-container {
    padding-top: 2rem;
}

.splash-box {
    background-color: #ffffff;
    padding: 45px;
    border-radius: 24px;
    text-align: center;
    border: 5px solid #f5c400;
    box-shadow: 0 0 30px rgba(245, 196, 0, 0.45);
}

.hero {
    background: linear-gradient(90deg, #000000, #252525);
    padding: 30px;
    border-radius: 20px;
    border-left: 10px solid #f5c400;
    margin-bottom: 25px;
}

.hero h1 {
    color: #f5c400;
    font-size: 44px;
    margin-bottom: 5px;
}

.hero p {
    color: white;
    font-size: 20px;
}

.card {
    background-color: #ffffff;
    color: #000000;
    padding: 22px;
    border-radius: 18px;
    border-top: 8px solid #f5c400;
    box-shadow: 0 6px 18px rgba(0,0,0,0.25);
    text-align: center;
}

.card h3 {
    color: #000000;
    margin-bottom: 10px;
}

.metric-value {
    color: #f5c400;
    font-size: 34px;
    font-weight: 800;
}

.section-title {
    color: #f5c400;
    font-size: 28px;
    font-weight: 800;
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)

# Splash screen
if not st.session_state.splash_done:
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown('<div class="splash-box">', unsafe_allow_html=True)
        st.image(GAME_LOGO, use_container_width=True)
        st.image(COMPANY_LOGO, width=280)
        st.markdown(
            "<h2 style='color:#000000;'>New Hire Scoring Dashboard</h2>",
            unsafe_allow_html=True
        )
        st.markdown("</div>", unsafe_allow_html=True)

    time.sleep(2)
    st.session_state.splash_done = True
    st.rerun()

# Home screen
else:
    st.markdown("""
    <div class="hero">
        <h1>Friday Night at the ER</h1>
        <p>New Hire Team Scoring Dashboard</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">Team Results</div>', unsafe_allow_html=True)

    teams = ["Team A", "Team B", "Team C", "Team D", "Team E"]
    cols = st.columns(5)

    for col, team in zip(cols, teams):
        with col:
            st.markdown(f"""
            <div class="card">
                <h3>{team}</h3>
                <p>Quality Errors</p>
                <div class="metric-value">0</div>
                <p>Total Cost</p>
                <div class="metric-value">$0</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">Dashboard Preview</div>', unsafe_allow_html=True)
    st.info("Next step: add score inputs, automatic calculations, rankings, and chart.")
