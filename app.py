import streamlit as st
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.neighbors import NearestNeighbors
from func_var import games_title
from func_var import hybrid_recommendation
from func_var import most_popular_games

st.title("Games Recommendation")

selected_game = st.selectbox(
   "Type or select a game",
   games_title['title'],
   index = None,
   placeholder = "Type or select a game",
   label_visibility = "collapsed"
)

if st.button('Show Recommendation'):
   recommendations = hybrid_recommendation(selected_game)
   data = recommendations
   with st.container(border = True):
      st.image(data.header_image[0], use_column_width = True)
      title = data.title[0]
      with st.popover(title, use_container_width = True):
         st.text("test")
         
   with st.container(border = True):
      st.image(data.header_image[1], use_column_width = True)
      title = data.title[1]
      with st.popover(title, use_container_width = True):
         st.text("test")
         
   with st.container(border = True):
      st.image(data.header_image[2], use_column_width = True)
      title = data.title[2]
      with st.popover(title, use_container_width = True):
         st.text("test")
   with st.container(border = True):
      st.image(data.header_image[3], use_column_width = True)
      title = data.title[3]
      with st.popover(title, use_container_width = True):
         st.text("test")
   with st.container(border = True):
      st.image(data.header_image[4], use_column_width = True)
      title = data.title[4]
      with st.popover(title, use_container_width = True):
         st.text("test")

st.header("Most popular games")
row1 = st.columns(3)
row2 = st.columns(3)
row3 = st.columns(3)
row4 = st.columns(3)
list_popular = most_popular_games()

index = 0
for col in row1 + row2 + row3 + row4:
   cont = col.container(border = True)
   cont.image(list_popular.loc[index,'header_image'])
   cont.text(list_popular.loc[index,'title'])
   index = index + 1

