from helper import extract_youtube_id, get_all_comments
import streamlit as st

def app():
  st.header('Phone Brands Sentiment Analysis', divider='rainbow')
  user_input = st.text_input("Enter a youtube link for sentiment analysis")
  if st.button('Submit', type="secondary"):
    try:
      the_youtube_id = extract_youtube_id(user_input)
      if the_youtube_id:
        with st.spinner("Please wait while we're loading the data..."):
          the_data = get_all_comments(the_youtube_id)
          st.write(f"Total Comments: {len(the_data)}")
          for data in the_data:
            st.write(data["comment"])
      else:
        st.write("Invalid youtube link.")
    except:
      st.write("Invalid youtube link.")
  else:
    st.write("Click the button to submit your link!")
    