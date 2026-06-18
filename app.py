import base64
import time
from pathlib import Path

import pandas as pd
import streamlit as st


st.set_page_config(
    page_title="PHI New Hire Scoring Dashboard",
    page_icon=":bar_chart:",
    layout="wide",
    initial_sidebar_state="collapsed",
)


APP_DIR = Path(__file__).parent
GAME_LOGO = APP_DIR / "1548433148198.png"
COMPANY_LOGO = APP_DIR / "PHI-Air-Med_logo-2023.jpg"
GOLD_LOGO = APP_DIR / "images.png"


def image_to_base64(path: Path) -> str:
    return base64.b64encode(path.read_bytes()).decode("utf-8")


game_logo_b64 = image_to_base64(GAME_LOGO)
company_logo_b64 = image_to_base64(COMPANY_LOGO)
gold_logo_b64 = image_to_base64(GOLD_LOGO)


TEAM_SCORES = pd.DataFrame(
    {
        "Team": ["Team A", "Team B", "Team C", "Team D", "Team E"],
        "Patients Served": [0, 0, 0, 0, 0],
        "Quality Errors": [0, 0, 0, 0, 0],
        "Total Cost": [0, 0, 0, 0, 0],
        "Score": [0, 0, 0, 0, 0],
    }
)


def inject_styles() -> None:
        unsafe_allow_html=True,
    )


def show_splash() -> None:
    st.markdown(
        f"""
        <div class="splash-screen">
            <div class="splash-panel">
                <div class="splash-logo-row">
                    <div class="splash-logo-card">
                        <img src="data:image/png;base64,{game_logo_b64}" alt="Friday Night at the ER logo">
                    </div>
                    <div class="splash-logo-card">
                        <img src="data:image/jpeg;base64,{company_logo_b64}" alt="PHI Air Medical logo">
                    </div>
                </div>
                <div class="splash-kicker">PHI Air Medical New Hire Experience</div>
                <h1 class="splash-title">Scoring Dashboard</h1>
                <p class="splash-subtitle">Loading the monthly board game command center</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def metric_tile(label: str, value: str, note: str) -> str:
    return f"""
    <div class="metric-tile">
        <div class="metric-label">{label}</div>
        <div class="metric-number">{value}</div>
        <div class="metric-note">{note}</div>
    </div>
    """


def team_card(team: str, score: int, errors: int, cost: int) -> str:
    return f"""
    <div class="team-card">
        <h3>{team}</h3>
        <div class="score-row">
            <span class="score-label">Score</span>
            <span class="score-value">{score}</span>
        </div>
        <div class="score-row">
            <span class="score-label">Quality Errors</span>
            <span class="score-value">{errors}</span>
        </div>
        <div class="score-row">
            <span class="score-label">Total Cost</span>
            <span class="score-value">${cost:,}</span>
        </div>
    </div>
    """


def show_home() -> None:
    st.markdown(
        f"""
        <div class="home-shell">
            <div class="topbar">
                <div class="brand-lockup">
                    <div class="brand-mark">
                        <img src="data:image/png;base64,{gold_logo_b64}" alt="PHI Air Medical mark">
                    </div>
                    <div>
                        <p class="brand-title">PHI Air Medical</p>
                        <p class="brand-subtitle">Friday Night at the ER scoring suite</p>
                    </div>
                </div>
                <div class="month-pill">Monthly New Hire Session</div>
            </div>

            <section class="hero">
                <div class="hero-content">
                    <div class="eyebrow">Professional scoring dashboard</div>
                    <h1>Friday Night at the ER</h1>
                    <p>
                        Capture monthly team results, track quality and cost performance, and review
                        the final leaderboard from one clean PHI-branded workspace.
                    </p>
                </div>
            </section>

            <div class="metric-strip">
                {metric_tile("Teams", "5", "Ready for monthly scoring")}
                {metric_tile("Current Leader", "--", "Scores have not been entered")}
                {metric_tile("Total Errors", "0", "Across all teams")}
                {metric_tile("Total Cost", "$0", "Calculated automatically")}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    entry_col, export_col, reset_col, spacer_col = st.columns([1.3, 1.3, 1.1, 3.3])
    with entry_col:
        st.button("Add Monthly Scores", use_container_width=True)
    with export_col:
        st.button("Export Score Sheet", use_container_width=True)
    with reset_col:
        st.button("Reset Session", use_container_width=True)

    st.markdown(
        """
        <div class="section-head">
            <div>
                <h2>Team Scoreboard</h2>
                <p>Initial layout for team score entry, calculation, and ranking.</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    cards = "".join(
        team_card(row["Team"], row["Score"], row["Quality Errors"], row["Total Cost"])
        for row in TEAM_SCORES.to_dict("records")
    )
    st.markdown(f'<div class="team-grid">{cards}</div>', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="section-head">
            <div>
                <h2>Final Score Graph</h2>
                <p>The chart is ready for live scoring data in the next build step.</p>
            </div>
        </div>
        <div class="chart-panel">
        """,
        unsafe_allow_html=True,
    )
    st.bar_chart(TEAM_SCORES.set_index("Team")[["Score"]], height=300)
    st.markdown("</div>", unsafe_allow_html=True)


inject_styles()

if "splash_done" not in st.session_state:
    st.session_state.splash_done = False

if not st.session_state.splash_done:
    show_splash()
    time.sleep(2)
    st.session_state.splash_done = True
    st.rerun()

show_home()
