from helper import extract_youtube_id, get_all_comments
import streamlit as st
import random
import pandas as pd
import numpy as np

st.header("💬 Youtube Comments Sentiment Analysis")

st.markdown("""
    <style>
      .stTextInput > label > div > p {
        font-size: 23px;
        padding: 0;
        margin: 0;
        font-weight: 600;
      }
    </style>
""", unsafe_allow_html=True)

user_input = st.text_input("Enter a youtube link for sentiment analysis")

sentiment_colors = {
    "Positive": "#28a745",  
    "Neutral": "#ffc107",   
    "Negative": "#dc3545"   
}

if st.button('Submit', type="secondary"):
  sentiments = ["Positive", "Neutral", "Negative"]
  try:
    the_youtube_id = extract_youtube_id(user_input)
    if the_youtube_id:
      with st.spinner("Please wait while we're loading the data..."):
        the_data = get_all_comments(the_youtube_id)
        data = np.random.choice(["Positive", "Neutral", "Negative"], size=len(the_data))

        sentiment_data = pd.DataFrame(data, columns=["Sentiment"])
        sentiment_counts = sentiment_data["Sentiment"].value_counts()
        positives = sentiment_counts.get("Positive", 0)
        neutrals = sentiment_counts.get("Neutral", 0)
        negatives = sentiment_counts.get("Negative", 0)
        st.balloons()
        st.markdown(f"""<p style="color: gray;">Total comments: {len(the_data)}</p>""", unsafe_allow_html=True)
        st.markdown(f"""<p style="color: green;">Positives: {positives}</p>""", unsafe_allow_html=True)
        st.markdown(f"""<p style="color: gray;">Neutrals: {neutrals}</p>""", unsafe_allow_html=True)
        st.markdown(f"""<p style="color: red;">Negatives: {negatives}</p>""", unsafe_allow_html=True)
        for index, data in enumerate(the_data):
          sentiment_color = sentiment_colors.get(sentiment_data.iloc[index, 0], "#6c757d")
          comment_html = f"""
              <div style="background-color: #f9f9f9; border: 1px solid #ddd; border-radius: 10px; padding: 20px; margin: 20px auto; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
                <p style="font-size: 18px; line-height: 1.6; color: #333; font-family: 'Arial', sans-serif;">
                  {data["comment"]}
                </p>
                <p style="font-size: 16px; color: gray; margin-top: 15px; font-family: 'Arial', sans-serif; font-weight: bold;">
                  Sentiment Analysis: <span style="color: {sentiment_color}; font-size: 18px; font-weight: bold; padding: 5px 10px; background-color: {sentiment_color + "33"}; border-radius: 5px;">
                    {sentiment_data.iloc[index, 0]}
                  </span>
                </p>
              </div>
            """

          st.markdown(comment_html, unsafe_allow_html=True)
    else:
      st.write("Invalid youtube link.")
  except Exception as e:
    print(e)
    st.write("Invalid youtube link.")
    