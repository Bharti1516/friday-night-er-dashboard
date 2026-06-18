import streamlit as st
import time
import base64

st.set_page_config(
    page_title="Friday Night at the ER",
    page_icon="🏥",
    layout="wide"
)

GAME_LOGO = "1548433148198.png"
COMPANY_LOGO = "PHI-Air-Med_logo-2023.jpg"

def image_to_base64(path):
    with open(path, "rb") as img:
        return base64.b64encode(img.read()).decode()

game_logo_b64 = image_to_base64(GAME_LOGO)
company_logo_b64 = image_to_base64(COMPANY_LOGO)

if "splash_done" not in st.session_state:
    st.session_state.splash_done = False

st.markdown("""
<style>
.stApp {
    background-color: #f5f6f8;
}

.block-container {
    padding-top: 0rem;
    max-width: 100%;
}

.splash-screen {
    height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
}

.splash-content {
    text-align: center;
}

.game-logo {
    width: 420px;
    max-width: 90%;
    margin-bottom: 28px;
}

.company-logo {
    width: 190px;
    max-width: 60%;
    margin-bottom: 25px;
}

.splash-title {
    font-size: 28px;
    font-weight: 800;
    color: #111111;
}

.splash-subtitle {
    font-size: 15px;
    color: #666666;
    margin-top: 8px;
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

.card {
    background-color: #ffffff;
    border-radius: 16px;
    padding: 22px;
    border: 1px solid #e5e7eb;
    border-top: 6px solid #f5c400;
    box-shadow: 0 4px 14px rgba(0,0,0,0.08);
    text-align: center;
}

.metric-value {
    color: #111111;
    font-size: 30px;
    font-weight: 800;
}
</style>
""", unsafe_allow_html=True)

if not st.session_state.splash_done:
    st.markdown(f"""
    <div class="splash-screen">
        <div class="splash-content">
            <img class="game-logo" src="data:image/png;base64,{game_logo_b64}">
            <br>
            <img class="company-logo" src="data:image/jpg;base64,{company_logo_b64}">
            <div class="splash-title">New Hire Team Scoring Dashboard</div>
            <div class="splash-subtitle">Powered by PHI Air Medical</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    time.sleep(2)
    st.session_state.splash_done = True
    st.rerun()

else:
    st.markdown("""
    <div class="app-header">
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
    st.info("Next step: score inputs, calculations, rankings, and chart.")
