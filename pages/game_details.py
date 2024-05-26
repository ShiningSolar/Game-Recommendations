import streamlit as st
from app import selected_game
from func_var import hybrid_recommendation

game_name = selected_game
recommendations = hybrid_recommendation(game_name)
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
