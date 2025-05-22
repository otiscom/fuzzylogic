import streamlit as st

home_page = st.Page(
    page="pages/home.py",
    title="Home",
    icon=":material/home:",
    default=True,
)

about_page = st.Page(
    page="pages/about.py",
    title="About",
    icon=":material/info:",
)

fuzzylogic_page = st.Page(
    page="pages/fuzzylogic.py",
    title="Fuzzy Logic",
    icon=":material/extension:",
)

pg = st.navigation(
    {
        "Main": [home_page, about_page],
        "AI": [fuzzylogic_page],
    }
)

st.sidebar.text("Made with ❤ by Niewiaro")

pg.run()
