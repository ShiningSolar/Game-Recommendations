import streamlit as st
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.neighbors import NearestNeighbors
from func_var import games_title
from func_var import hybrid_recommendation
from func_var import most_popular_games

st.set_page_config(
    page_title="Home",
    layout="wide",
    initial_sidebar_state="auto"
)

st.title("Games Recommendation")

selected_game = st.selectbox(
   "Type or select a game",
   games_title['title'],
   index = None,
   placeholder = "Type or select a game",
   label_visibility = "collapsed"
)


if st.button('Show Recommendation'):
   #selection = str(selected_game)
   st.query_params.game_name = selected_game
   st.switch_page("pages/game_details.py")

st.header("Most popular games")
row1 = st.columns(3)
row2 = st.columns(3)
row3 = st.columns(3)
row4 = st.columns(3)
list_popular = most_popular_games()

index = 0
for col in row1 + row2 + row3 + row4:
   image = list_popular.loc[index,'header_image']
   title = list_popular.loc[index,'title']
   cont = col.container(border = True)
   cont.image(image)
   cont.text(title)
   if cont.button(title):
      st.query_params.game_name = title
      st.switch_page("pages/game_details.py")
   index = index + 1

