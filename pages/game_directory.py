import streamlit as st
import pandas as pd
from func_var import genre_filtering

genres = ["Racing", "Adventure", "Sports", "Strategy", "Casual", "RPG", "Simulation", "Action", "Indie"]

num_of_page = 1 
index = 0

def genre_change():
  st.session_state['index'] = 0
  st.session_state['page'] = 1
  st.session_state['next'] = 1
  st.session_state['back'] = 1
  st.session_state['next_button_state'] = False
  st.session_state['back_button_state'] = True

def change_page(name):
  st.write(name)
  st.session_state['name'] = name
  st.session_state['details_page'] = True

if 'details_page' not in st.session_state :
  st.session_state['details_page'] = False

if st.session_state['details_page'] == True:
  st.query_params.game_name = st.session_state['name']
  st.session_state['details_page'] = False
  for key in st.session_state.keys():
    del st.session_state[key]
  st.switch_page("pages/game_details.py")
  
def show_data(index):
  a = row1.columns(3)
  b = row2.columns(3)
  c = row3.columns(3)
  d = row4.columns(3)
  
  if 'index' not in st.session_state:
    st.session_state['index'] = str(index)
  
  #index = int(st.session_state['index'])
  
  for col in a + b + c + d:
    if index < len(list_popular):
      cont = col.container(border = True)
      title = list_popular.loc[index,'title']
      cont.image(list_popular.loc[index,'header_image'])
      cont.button(title, on_click = change_page, args = [title], use_container_width = True)
        
      index = index + 1
    else :
      st.session_state['next_button_state'] = True
      break

  #i = index
  st.session_state['index'] = str(index)

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
  st.session_state['back'] = st.session_state['page']
  st.session_state['back_button_state'] = False


def back_func():
  num_of_page = st.session_state['page']
  st.session_state['back'] = num_of_page -1
  if st.session_state['back'] == 1:
      st.session_state['back_button_state'] = True
  index = int(st.session_state['index'])
  index = index - 24 + ((12 * num_of_page) - index)
  st.session_state['index'] = str(index)
  st.session_state['page'] = st.session_state['back']
  st.session_state['next'] = st.session_state['page']
  st.session_state['next_button_state'] = False
 
if 'list_genre' not in st.session_state:
  st.session_state['list_genre'] = None
  
if 'list_genre' in st.session_state:
  selected_genres = st.session_state['list_genre']

genre_options = st.multiselect(
  "What are your favorite colors",
  options = genres,
  default = selected_genres,
  placeholder = "Pilih genre game yang diinginkan",
  label_visibility = "collapsed",
  on_change = genre_change
)
#else :
#  genre_options = st.multiselect(
#    "What are your favorite colors",
#    options = genres,
#    default = st.session_state['list_genre'],
#    placeholder = "Pilih genre game yang diinginkan",
#    label_visibility = "collapsed",
#    on_change = genre_change
#  )
  
st.session_state['list_genre'] = genre_options
list_popular = genre_filtering(genre_options)


st.title("Daftar Game")
row1 = st.empty()
row2 = st.empty()
row3 = st.empty()
row4 = st.empty()   

buff1, back_button, page_number, next_button, buff2 = st.columns([3,1,1,1,3])
page_text = page_number.empty()

if 'page' not in st.session_state :
  st.session_state['page'] = num_of_page
  show_data(index)
  page_text.markdown(f"""{num_of_page}""")
  st.session_state['back_button_state'] = True
  st.session_state['next_button_state'] = False
elif 'page' in st.session_state :
  x = int(st.session_state['page'])
  index = (12*x)-12
  #if st.session_state['next
  page_text.markdown(f"""{st.session_state['page']}""")
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

#how to pevent index terus betambah tanpa mengklik apapun
#change var i to var index in show_data()
