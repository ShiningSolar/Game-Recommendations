import streamlit as st
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.neighbors import NearestNeighbors
from func_var import games_title
from func_var import hybrid_recommendation

st.header("Games Recommendation")

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
      
def unused(cols, recommendations) :
   index=0
   for col in cols:
      data = recommendations[index]
      col.text(data[0])
      col.image(data[1])
      index= index + 1
   
