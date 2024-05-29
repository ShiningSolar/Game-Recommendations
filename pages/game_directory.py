import streamlit as st
import pandas as pd
from func_var import genre_filtering

st.title("Daftar Game")
genres = ["Racing", "Adventure", "Sports", "Strategy", "Casual", "RPG", "Simulation", "Action", "Indie"]

def genre_change():
  st.write('genre change')
  st.session_state['index'] = 0
  st.session_state['page'] = 1

options = st.multiselect(
  "What are your favorite colors",
  options = genres,
  default = None,
  placeholder = "Pilih genre game yang diinginkan",
  label_visibility = "collapsed",
  on_change = genre_change
)

#st.write("You selected:", options)
row1 = st.empty()
row2 = st.empty()
row3 = st.empty()
row4 = st.empty()
list_popular = genre_filtering(options)
num_of_page = 1 
index = 0

def show_data(i):
  a = row1.columns(3)
  b = row2.columns(3)
  c = row3.columns(3)
  d = row4.columns(3)
  
  if 'index' not in st.session_state:
    st.session_state['index'] = str(i)
    
  index =  int(st.session_state['index'])

  st.write('index var di dalam show_data')
  st.write(index)
  
  for col in a + b + c + d:
    if index < len(list_popular):
      cont = col.container(border = True)
      title = list_popular.loc[index,'title']
      cont.image(list_popular.loc[index,'header_image'])
      cont.text(index)
      if cont.button(title, use_container_width = True):
        st.query_params.game_name = title
        st.switch_page("pages/game_details.py")
      index = index + 1
    else :
      st.session_state['next_button_state'] = True
      break

  i = index
  st.session_state['index'] = str(i)
  st.write('index state di dalam show_data')
  st.write(st.session_state['index'])
  
def switch_page():
  row1.empty()
  row2.empty()
  row3.empty()
  row4.empty()
  #show_data(index)

def next_func():
  if 'next' not in st.session_state:
    st.session_state['next'] = 2
    st.session_state['page'] = st.session_state['next']
    index = int( st.session_state['index'])
  else :
    num_of_page = st.session_state['next']
    st.session_state['next'] = num_of_page + 1
    index = int( st.session_state['index'])
    st.session_state['page'] = st.session_state['next']
  st.session_state['back_button_state'] = False


def back_func():
  num_of_page = st.session_state['page']
  st.session_state['back'] = num_of_page -1
  #st.session_state['page'] = st.session_state['back']
  if st.session_state['back'] == 1:
      st.session_state['back_button_state'] = True
  index = int(st.session_state['index'])
  index = index - 24
  st.session_state['index'] = str(index)
  st.session_state['page'] = st.session_state['back']
  st.write('index var in back func')
  st.write(index)
  st.write('index state in back func')
  st.write(st.session_state['index'])
    

buff1, back_button, page_number, next_button, buff2 = st.columns([3,1,1,1,3])
page_text = page_number.empty()

if 'page' not in st.session_state :
  st.session_state['page'] = num_of_page
  show_data(index)
  page_text.markdown(f"""{num_of_page}""")
  st.session_state['back_button_state'] = True
  st.session_state['next_button_state'] = False
elif st.session_state.get('page') :
  st.session_state['next'] = st.session_state['page']
  st.session_state['back'] = st.session_state['page']
  index = int(st.session_state['index'])
  st.write('index var in get index')
  st.write(index)
  show_data(index)
  
if st.session_state.get('next') :
  page_text.empty()
  page_text.markdown(f"""{st.session_state['next']}""")

if st.session_state.get('back') :
  page_text.empty()
  page_text.markdown(f"""{st.session_state['back']}""")

back_button.button('back', on_click = back_func, disabled = st.session_state['back_button_state'])
next_button.button('next', on_click = next_func, disabled = st.session_state['next_button_state'])
    

st.session_state


#make button use on_click, inside onclick function add session state
#still haven't figure it out how button works
