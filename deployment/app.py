import streamlit as st
import home
import youtube
st.set_page_config(layout="wide")
st.title("Phone Brands Sentiment Analysis")

tab1, tab2 = st.tabs(["Word Clouds", "Youtube Comments Analysis"])

def hide_tabbar():
    st.sidebar.empty()

with tab1:
    st.markdown(
        """
        <style>
        .css-1d391kg {
            display: block;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    home.app()

with tab2:
    st.markdown(
        """
        <style>
        .css-1d391kg {
            display: none;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    youtube.app()