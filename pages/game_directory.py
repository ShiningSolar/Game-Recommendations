import streamlit as st
import pandas as pd
from func_var import genre_filtering

st.title("Daftar Game")
genres = ["Racing", "Adventure", "Sports", "Strategy", "Casual", "RPG", "Simulation", "Action", "Indie"]

options = st.multiselect(
  "What are your favorite colors",
  options = genres,
  default = None,
  placeholder = "Pilih genre game yang diinginkan",
  label_visibility = "collapsed"
)

#st.write("You selected:", options)
row1 = st.empty()
row2 = st.empty()
row3 = st.empty()
row4 = st.empty()
list_popular = genre_filtering(options)
num_of_item = len(list_popular)
num_of_page = 1 

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
  else:
    st.query_params.index = index
  st.session_state.x = int(st.query_params.index)
  
def switch_page(index):
  row1.empty()
  row2.empty()
  row3.empty()
  row4.empty()
  index = st.session_state.x
  show_data(index)
  
show_data()

def next_func():
  st.session_state['next'] = num_of_page + 1

def back_func():
  st.session_state['back'] == num_of_page - 1  

buff1, back_button, page_number, next_button, buff2 = st.columns([3,1,1,1,3])
page_number.markdown(f"""**{num_of_page}**""")
back_button.button('back', on_click = back_func)
next_button.button('next', on_click = next_func)

if 'back' not in st.session_state:
  st.session_state['back'] = num_of_page
else :
  if st.session_state['back'] == num_of_page - 1 :
    st.write('back')
    
if 'next' not in st.session_state:
  st.session_state['next'] = num_of_page
else :
  if st.session_state['next'] == num_of_page + 1:
    num_of_page = st.session_state['next']
    st.write('next')
    switch_page()

st.session_state
st.write(num_of_item)


#make button use on_click, inside onclick function add session state
