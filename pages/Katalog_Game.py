import streamlit as st
import pandas as pd
import streamlit_antd_components as sac
from func_var import genre_filtering

st.set_page_config(
    page_title="Katalog Game",
    page_icon="📃",
    layout="wide",
    initial_sidebar_state="auto"
)

genres = ["Racing", "Adventure", "Sports", "Strategy", "Casual", "RPG", "Simulation", "Action", "Indie"]
num_of_page = 1 
index = 0

def genre_change():
  st.session_state.list_genre = st.session_state.temp_list_genre
  st.session_state['index'] = 0
  st.session_state['page'] = 1
  #st.session_state['next'] = 1
  #st.session_state['back'] = 1
  #st.session_state['next_button_state'] = False
  #st.session_state['back_button_state'] = True
  return

#def pagination_change():
  #st.session_state.page = st.session_state.temp_page
  #st.session_state['index'] = 0
  #return

def change_page(name):
  st.session_state['name'] = name
  st.session_state['details_page'] = True
  
if 'details_page' not in st.session_state :
  st.session_state['details_page'] = False
if st.session_state['details_page'] == True:
  st.query_params.game_name = st.session_state['name']
  st.session_state['details_page'] = False
  st.switch_page("pages/game_details.py")
  
def show_data(index):
  a = row1.columns(3)
  b = row2.columns(3)
  c = row3.columns(3)
  d = row4.columns(3)
  if 'index' not in st.session_state:
    st.session_state['index'] = str(index)
  for col in a + b + c + d:
    if index < len(list_popular):
      cont = col.container(border = True)
      title = list_popular.loc[index,'title']
      cont.image(list_popular.loc[index,'header_image'])
      cont.button(title, on_click = change_page, args = [title], use_container_width = True)
      index = index + 1
    else :
      #st.session_state['next_button_state'] = True
      break 
  st.session_state['index'] = str(index)

#def next_func():
#  if 'next' not in st.session_state:
    #st.session_state['next'] = 2
    #st.session_state['page'] = st.session_state['next']
#    index = int( st.session_state['index'])
#  else :
#    num_of_page = st.session_state['next']
    #st.session_state['next'] = num_of_page + 1
#    index = int( st.session_state['index'])
#    st.session_state['page'] = st.session_state['next']
#  st.session_state['back'] = st.session_state['page']
  #st.session_state['back_button_state'] = False
  
#def back_func():
#  num_of_page = st.session_state['page']
#  st.session_state['back'] = num_of_page -1
  #if st.session_state['back'] == 1:
  #    st.session_state['back_button_state'] = True
#  index = int(st.session_state['index'])
#  index = index - 24 + ((12 * num_of_page) - index)
#  st.session_state['index'] = str(index)
#  st.session_state['page'] = st.session_state['back']
  #st.session_state['next'] = st.session_state['page']
  #st.session_state['next_button_state'] = False

if 'list_genre' not in st.session_state :
  st.session_state['list_genre'] = []

st.session_state['temp_list_genre'] = st.session_state['list_genre']

genre_options = st.multiselect(
  "What are your favorite colors",
  options = genres,
  key = "temp_list_genre",
  default = st.session_state['list_genre'],
  placeholder = "Pilih genre game yang diinginkan",
  label_visibility = "collapsed",
  on_change = genre_change
)
st.session_state['list_genre'] = genre_options

#genre_options = sac.cascader(items=genres, index=st.session_state['list_genre'], placeholder='Pilih genre game yang diinginkan', color='indigo', multiple=True, search=True, clear=True, key = 'temp_list_genre', on_change = genre_change)
#st.session_state['list_genre'] = genre_options

list_popular = genre_filtering(st.session_state['list_genre'])
total_game = len(list_popular)
st.title("Daftar Game")
row1 = st.empty()
row2 = st.empty()
row3 = st.empty()
row4 = st.empty()
#buff1, back_button, page_number, next_button, buff2 = st.columns([3,1,1,1,3])
#page_text = page_number.empty()

pagination = sac.pagination(total=total_game, page_size=12, align='center', variant='filled', simple=True)
st.session_state['page'] = pagination

if 'page' not in st.session_state :
  st.session_state['page'] = pagination
  show_data(index)
  #page_text.markdown(f"""{num_of_page}""")
  #st.session_state['back_button_state'] = True
  #st.session_state['next_button_state'] = False
elif 'page' in st.session_state :
  x = int(st.session_state['page'])
  index = (12*x)-12
  #if st.session_state['next
  #page_text.markdown(f"""{st.session_state['page']}""")
  show_data(index)

#if st.session_state.get('next') :
#  page_text.empty()
#  page_text.markdown(f"""{st.session_state['next']}""")
#if st.session_state.get('back') :
#  page_text.empty()
#  page_text.markdown(f"""{st.session_state['back']}""")

#st.session_state['temp_page'] = st.session_state['page']
#pagination
#pagination = sac.pagination(total=total_game, page_size=12, align='center', variant='filled', simple=True, on_change = pagination_change, key = "temp_page")
#st.session_state['page'] = pagination

#back_button.button('back', on_click = back_func, disabled = st.session_state['back_button_state'])
#next_button.button('next', on_click = next_func, disabled = st.session_state['next_button_state'])

#st.session_state
