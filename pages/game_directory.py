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

#st.write("You selected:", options)
list_popular = genre_filtering(options)

def show_data(index = 0):
  row1 = st.columns(3)
  row2 = st.columns(3)
  row3 = st.columns(3)
  row4 = st.columns(3)
  list_popular = genre_filtering(options)
  for col in row1 + row2 + row3 + row4:
    cont = col.container(border = True)
    title = list_popular.loc[index,'title']
    cont.image(list_popular.loc[index,'header_image'])
    #cont.text(list_popular.loc[index,'title'])
    if cont.button(title, use_container_width = True):
      st.query_params.game_name = title
      st.switch_page("pages/game_details.py")
    index = index + 1
  return index, list_popular
    
last_index = show_data()


num_of_item = len(list_popular)
st.write(num_of_item)

def switch_page(last_index):
  last_index, list_popular = show_data(last_index)
  return last_index

buff1, back_button, page_number, next_button, buff2 = st.columns([3,1,0.5,1,3])
num_of_page = 1
page_number.markdown(f"""**{num_of_page}**""")
if back_button.button('Back'):
  st.write('back')
if next_button.button('Next'):
  st.write('next')
  next_index = switch_page(last_index)
  
