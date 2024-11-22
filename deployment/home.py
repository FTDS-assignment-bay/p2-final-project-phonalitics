import streamlit as st
from wordcloud import WordCloud
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import os
import re

st.header("🔥 Phone Brands Word Clouds")

data = pd.read_csv("final_dataset_text_processed.csv")
data.dropna(inplace=True)
val = st.sidebar.pills("Choose Phone Word Clouds To Show", data["tipe_produk"].unique(), selection_mode="multi", default="Galaxy S24")
for the_value in val:
  the_product = data[data["tipe_produk"] == the_value]
  if not the_product.empty:
    text_data = " ".join(data["text_processed"])
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text_data)
    regex = re.compile(r"^(.*)\.[^.]+$")
    col1, col2 = st.columns([2.5, 7.5])
    image = None
    
    for item in os.listdir("images"):
      item_cleaned = regex.match(item).group(1)
      if item_cleaned.lower().strip() == the_value.lower().strip():
        image = Image.open(f"./images/{item}")
        break
    with col1:
      if image:
        st.markdown(f"### {the_value}")
        st.image(image, caption=f"{the_value} Image")

    with col2:
      st.markdown(f"### Word Cloud for {the_value}")

      plt.figure(figsize=(10, 5))
      plt.imshow(wordcloud, interpolation='bilinear')
      plt.axis("off")
      st.pyplot(plt)

      st.write('<div style="padding: 10px;"></div>', unsafe_allow_html=True)