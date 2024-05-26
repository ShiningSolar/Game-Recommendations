import streamlit as st
import panda as pd

st.title("Daftar Game")
genres = ["Racing", "Adventure", "Sports", "Strategy", "Casual", "RPG", "Simulation", "Action", "Indie"]

options = st.multiselect(
  "What are your favorite colors",
  option = genres,
  default = None,
  placeholder = "Choose your game genre",
  label_visibility = "collapsed"
)

st.write("You selected:", options)
