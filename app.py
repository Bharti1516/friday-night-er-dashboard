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
    background-color: #ffffff;
}

.block-container {
    padding-top: 2rem;
}

.splash {
    text-align: center;
    padding-top: 80px;
}

.home-header {
    background-color: #000000;
    padding: 28px;
    border-radius: 16px;
    border-bottom: 6px solid #f5c400;
    color: white;
    margin-bottom: 30px;
}

.home-header h1 {
    color: #f5c400;
    margin-bottom: 5px;
}

.card {
    background-color: #ffffff;
    border: 1px solid #e6e6e6;
    border-top: 6px solid #f5c400;
    border-radius: 14px;
    padding: 22px;
    text-align: center;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
}

.card h3 {
    color: #000000;
}

.metric-value {
    font-size: 30px;
    font-weight: 800;
    color: #000000;
}
</style>
""", unsafe_allow_html=True)

# Splash screen
if not st.session_state.splash_done:
    st.markdown('<div class="splash">', unsafe_allow_html=True)

    st.image(GAME_LOGO, width=420)
    st.markdown("<br>", unsafe_allow_html=True)
    st.image(COMPANY_LOGO, width=220)

    st.markdown("</div>", unsafe_allow_html=True)

    time.sleep(2)
    st.session_state.splash_done = True
    st.rerun()

# Home screen
else:
    st.markdown("""
    <div class="home-header">
        <h1>Friday Night at the ER</h1>
        <p>New Hire Team Scoring Dashboard</p>
    </div>
    """, unsafe_allow_html=True)

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

    st.divider()
    st.subheader("Dashboard Preview")
    st.info("Next step: add score inputs, automatic calculations, rankings, and chart.")
