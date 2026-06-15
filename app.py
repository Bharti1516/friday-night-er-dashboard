import streamlit as st

st.set_page_config(
    page_title="Friday Night at the ER",
    page_icon="🏥",
    layout="wide"
)

# --------------------------------------------------
# APP STATE
# --------------------------------------------------

if "started" not in st.session_state:
    st.session_state.started = False

# --------------------------------------------------
# CUSTOM STYLING
# --------------------------------------------------

st.markdown("""
<style>

.stApp {
    background-color: #111111;
}

.main-title {
    color: #f5c400;
    text-align: center;
    font-size: 48px;
    font-weight: bold;
}

.subtitle {
    color: white;
    text-align: center;
    font-size: 22px;
}

.team-card {
    background-color: #1f1f1f;
    border-left: 6px solid #f5c400;
    padding: 20px;
    border-radius: 12px;
    text-align: center;
}

.team-card h3 {
    color: #f5c400;
}

.team-card p {
    color: white;
}

.start-button {
    text-align:center;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# SPLASH SCREEN
# --------------------------------------------------

if not st.session_state.started:

    st.markdown("<br><br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1,2,1])

    with col2:

        try:
            st.image("1548433148198.png", width=450)
        except:
            st.warning("Friday Night at the ER logo not found")

        st.markdown("<br>", unsafe_allow_html=True)

        try:
            st.image("PHI-Air-Med_logo-2023.jpg", width=300)
        except:
            st.warning("PHI logo not found")

        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown(
            "<h2 class='subtitle'>New Hire Scoring Dashboard</h2>",
            unsafe_allow_html=True
        )

        st.markdown("<br>", unsafe_allow_html=True)

        if st.button("🚀 Start Dashboard", use_container_width=True):
            st.session_state.started = True
            st.rerun()

# --------------------------------------------------
# HOME PAGE
# --------------------------------------------------

else:

    st.markdown(
        "<h1 class='main-title'>Friday Night at the ER</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<p class='subtitle'>Team Performance Dashboard</p>",
        unsafe_allow_html=True
    )

    st.divider()

    col1, col2, col3, col4, col5 = st.columns(5)

    teams = ["Team A", "Team B", "Team C", "Team D", "Team E"]

    for col, team in zip(
        [col1, col2, col3, col4, col5],
        teams
    ):
        with col:
            st.markdown(
                f"""
                <div class="team-card">
                    <h3>{team}</h3>
                    <p>Quality Errors</p>
                    <h2>0</h2>
                    <p>Total Cost</p>
                    <h2>$0</h2>
                </div>
                """,
                unsafe_allow_html=True
            )

    st.divider()

    st.subheader("📊 Results")

    st.info(
        "This is the prototype dashboard. "
        "Next we will add score entry, calculations, rankings and charts."
    )
