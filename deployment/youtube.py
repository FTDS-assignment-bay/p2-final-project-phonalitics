from helper import extract_youtube_id, get_all_comments
import streamlit as st
import random

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
        st.balloons()
        st.markdown(f"""<p style="color: green; padding: 0; margin: 0;">Total comments: {len(the_data)}</p>""", unsafe_allow_html=True)
        for data in the_data:
          sentiment = random.choice(sentiments)
          sentiment_color = sentiment_colors.get(sentiment, "#6c757d")
          comment_html = f"""
          <div style="background-color: #f9f9f9; border: 1px solid #ddd; border-radius: 10px; padding: 20px; margin: 20px auto; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
            <p style="font-size: 18px; line-height: 1.6; color: #333; font-family: 'Arial', sans-serif;">
              {data["comment"]}
            </p>
            <p style="font-size: 16px; margin-top: 15px; font-family: 'Arial', sans-serif; font-weight: bold;">
              Sentiment Analysis: <span style="color: {sentiment_color}; font-size: 18px; font-weight: bold; padding: 5px 10px; background-color: {sentiment_color + "33"}; border-radius: 5px;">
                {sentiment}
              </span>
            </p>
          </div>
          """

          st.markdown(comment_html, unsafe_allow_html=True)
    else:
      st.write("Invalid youtube link.")
  except:
    st.write("Invalid youtube link.")
    