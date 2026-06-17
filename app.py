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
    background: radial-gradient(circle at top, #2b2b2b 0%, #111111 45%, #000000 100%);
    color: white;
}

.block-container {
    padding-top: 2rem;
}

.splash-wrapper {
    max-width: 760px;
    margin: 0 auto;
    padding-top: 40px;
    text-align: center;
}

.logo-card {
    background: #ffffff;
    border-radius: 22px;
    padding: 30px;
    border: 3px solid #f5c400;
    box-shadow: 0 10px 35px rgba(0,0,0,0.45);
}

.company-logo {
    background: white;
    border-radius: 14px;
    padding: 10px;
    display: inline-block;
    margin-top: 22px;
}

.splash-title {
    color: #f5c400;
    font-size: 30px;
    font-weight: 800;
    margin-top: 28px;
}

.splash-subtitle {
    color: #ffffff;
    font-size: 16px;
    margin-top: 6px;
}

.heartbeat {
    color: #f5c400;
    font-size: 30px;
    letter-spacing: 3px;
    margin-top: 20px;
    animation: pulse 1.2s infinite;
}

.loading-text {
    color: #ffffff;
    font-size: 15px;
    margin-top: 12px;
}

@keyframes pulse {
    0% { opacity: 0.35; transform: scale(0.98); }
    50% { opacity: 1; transform: scale(1.03); }
    100% { opacity: 0.35; transform: scale(0.98); }
}

.hero {
    background: linear-gradient(90deg, #000000, #262626);
    padding: 28px;
    border-radius: 18px;
    border-left: 10px solid #f5c400;
    margin-bottom: 25px;
}

.hero h1 {
    color: #f5c400;
    font-size: 42px;
    margin-bottom: 5px;
}

.hero p {
    color: white;
    font-size: 18px;
}

.card {
    background: #ffffff;
    color: #000000;
    padding: 22px;
    border-radius: 16px;
    border-top: 7px solid #f5c400;
    box-shadow: 0 6px 18px rgba(0,0,0,0.25);
    text-align: center;
}

.card h3 {
    color: #000000;
}

.metric-value {
    color: #000000;
    font-size: 30px;
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

# -----------------------------
# Splash screen
# -----------------------------
if not st.session_state.splash_done:
    st.markdown("""
    <div class="splash-wrapper">
        <div class="logo-card">
    """, unsafe_allow_html=True)

    st.image(GAME_LOGO, width=520)

    st.markdown('<div class="company-logo">', unsafe_allow_html=True)
    st.image(COMPANY_LOGO, width=210)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("""
        </div>
        <div class="splash-title">New Hire Simulation Dashboard</div>
        <div class="splash-subtitle">Powered by PHI Air Medical</div>
        <div class="heartbeat">▁▂▃▅▇▅▃▂▁  Initializing  ▁▂▃▅▇▅▃▂▁</div>
        <div class="loading-text">Loading dashboard...</div>
    </div>
    """, unsafe_allow_html=True)

    time.sleep(2)
    st.session_state.splash_done = True
    st.rerun()

# -----------------------------
# Home screen
# -----------------------------
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
    st.info("Next step: add score inputs, calculations, rankings, and chart.")
