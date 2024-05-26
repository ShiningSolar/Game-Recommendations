import streamlit as st
import pandas as pd
from func_var import genre_filtering

st.title("Daftar Game")
genres = ["Racing", "Adventure", "Sports", "Strategy", "Casual", "RPG", "Simulation", "Action", "Indie"]

options = st.multiselect(
  "What are your favorite colors",
  options = genres,
  default = None,
  placeholder = "Choose your game genre",
  label_visibility = "collapsed"
)

st.write("You selected:", options)

row1 = st.columns(3)
row2 = st.columns(3)
row3 = st.columns(3)
row4 = st.columns(3)
list_popular = genre_filtering()

index = 0
for col in row1 + row2 + row3 + row4:
   cont = col.container(border = True)
   cont.image(list_popular.loc[index,'header_image'])
   cont.text(list_popular.loc[index,'title'])
   index = index + 1
