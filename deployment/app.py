import streamlit as st
import home
import youtube

PAGES = {
    "Home": home,
    "Youtube": youtube
}
st.sidebar.title('Navigation')

selection = st.sidebar.selectbox("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()