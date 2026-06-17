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
    background-color: #f5f6f8;
}

.block-container {
    padding-top: 2rem;
    max-width: 1200px;
}

.splash-wrapper {
    height: 80vh;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
}

.splash-title {
    margin-top: 28px;
    font-size: 28px;
    font-weight: 800;
    color: #111111;
}

.splash-subtitle {
    margin-top: 8px;
    font-size: 15px;
    color: #666666;
}

.app-header {
    background-color: #111111;
    border-bottom: 6px solid #f5c400;
    padding: 24px 30px;
    border-radius: 16px;
    color: white;
    margin-bottom: 28px;
}

.app-header h1 {
    color: #f5c400;
    font-size: 38px;
    margin-bottom: 4px;
}

.app-header p {
    color: #ffffff;
    font-size: 17px;
    margin: 0;
}

.card {
    background-color: #ffffff;
    border-radius: 16px;
    padding: 22px;
    border: 1px solid #e5e7eb;
    border-top: 6px solid #f5c400;
    box-shadow: 0 4px 14px rgba(0,0,0,0.08);
    text-align: center;
}

.card h3 {
    color: #111111;
    margin-bottom: 12px;
}

.label {
    color: #666666;
    font-size: 14px;
    margin-bottom: 2px;
}

.metric-value {
    color: #111111;
    font-size: 30px;
    font-weight: 800;
    margin-bottom: 14px;
}

.section-title {
    color: #111111;
    font-size: 26px;
    font-weight: 800;
    margin-top: 24px;
    margin-bottom: 14px;
}
</style>
""", unsafe_allow_html=True)

# Splash screen
if not st.session_state.splash_done:
    st.markdown('<div class="splash-wrapper"><div>', unsafe_allow_html=True)

    st.image(GAME_LOGO, width=420)
    st.markdown("<br>", unsafe_allow_html=True)
    st.image(COMPANY_LOGO, width=180)

    st.markdown("""
        <div class="splash-title">New Hire Team Scoring Dashboard</div>
        <div class="splash-subtitle">Powered by PHI Air Medical</div>
    """, unsafe_allow_html=True)

    st.markdown("</div></div>", unsafe_allow_html=True)

    time.sleep(2)
    st.session_state.splash_done = True
    st.rerun()

# Home screen
else:
    st.markdown("""
    <div class="app-header">
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
                <div class="label">Quality Errors</div>
                <div class="metric-value">0</div>
                <div class="label">Total Cost</div>
                <div class="metric-value">$0</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">Dashboard Preview</div>', unsafe_allow_html=True)
    st.info("Next step: add score inputs, automatic calculations, rankings, and chart.")
