import streamlit as st
from wordcloud import WordCloud
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import os
import re

def app():
    st.header('Phone Brands Sentiment Analysis', divider='rainbow')
    data = pd.read_csv("final_dataset_text_processed.csv")
    data.dropna(inplace=True)
    val = st.sidebar.pills("Choose Phone Word Cloud To Show", data["tipe_produk"].unique(), selection_mode="multi")
    for the_value in val:
      the_product = data[data["tipe_produk"] == the_value]
      if not the_product.empty:
        text_data = " ".join(data["text_processed"])
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text_data)
        regex = re.compile(r"^(.*)\.[^.]+$")
        col1, col2 = st.columns([3, 7])
        image = None
        
        for item in os.listdir("images"):
          item_cleaned = regex.match(item).group(1)
          if item_cleaned.lower().strip() == the_value.lower().strip():
            image = Image.open(f"./images/{item}")
            break
        with col1:
          if image:
            st.write(the_value)
            st.image(image)
        plt.title(f"Wordcloud for phone {the_value}")
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        with col2:
          st.write('<p style="visibility: hidden;">This is some text.</p>', unsafe_allow_html=True)
          st.pyplot(plt)