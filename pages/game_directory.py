import streamlit as st
import pandas as pd

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
