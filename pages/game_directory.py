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
row1 = st.empty()
row2 = st.empty()
row3 = st.empty()
row4 = st.empty()
list_popular = genre_filtering(options)


def show_data(index = 0):
  a = row1.columns(3)
  b = row2.columns(3)
  c = row3.columns(3)
  d = row4.columns(3)
  for col in a + b + c + d:
    cont = col.container(border = True)
    title = list_popular.loc[index,'title']
    cont.image(list_popular.loc[index,'header_image'])
    if cont.button(title, use_container_width = True):
      st.query_params.game_name = title
      st.switch_page("pages/game_details.py")
    index = index + 1
  if 'index' not in st.query_params:
    st.query_params.index = index
  
  
def switch_page(index):
  row1.empty()
  row2.empty()
  row3.empty()
  row4.empty()
  last_index = show_data(index)
  st.write(last_index)
  return last_index
  
show_data()


buff1, back_button, page_number, next_button, buff2 = st.columns([3,1,0.5,1,3])
num_of_page = 1
num_of_item = len(list_popular)

page_number.markdown(f"""**{num_of_page}**""")
if back_button.button('Back'):
  st.write('back')
if next_button.button('Next'):
  st.write('next')
  #index = last_index
  #next_index = switch_page(index)
  #last_index = next_index


st.write(num_of_item)
