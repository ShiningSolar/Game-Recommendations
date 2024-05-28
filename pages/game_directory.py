import streamlit as st
import pandas as pd
from func_var import genre_filtering

st.title("Daftar Game")
genres = ["Racing", "Adventure", "Sports", "Strategy", "Casual", "RPG", "Simulation", "Action", "Indie"]

def genre_change():
  st.write('genre change')
  st.session_state['index'] = 0

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
num_of_item = len(list_popular)
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
  #if st.session_state.get('back') :
    #index = index - 12
  st.write('index di dalam func')
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
      break

    i = index
    st.session_state['index'] = str(i)
  
def switch_page():
  row1.empty()
  row2.empty()
  row3.empty()
  row4.empty()
  #show_data(index)


show_data(index)


def next_func():
  if 'next' not in st.session_state:
    st.session_state['next'] = 2
    st.session_state['page'] = st.session_state['next']
    index = int( st.session_state['index'])
    switch_page()
  else :
    num_of_page = st.session_state['next']
    st.session_state['next'] = num_of_page + 1
    index = int( st.session_state['index'])
    st.session_state['page'] = st.session_state['next']
    switch_page()
  st.session_state['button_state'] = False


def back_func():
  num_of_page = st.session_state['page']
  st.session_state['back'] = num_of_page -1
  #st.session_state['page'] = st.session_state['back']
  if st.session_state['back'] == 1:
      st.session_state['button_state'] = True
  index = int(st.session_state['index'])
  st.session_state['index'] = str(index - 12)
  st.session_state['page'] = st.session_state['back']
  switch_page()
  show_data(int(st.session_state['index']))
  
  st.write(st.session_state['index'])
    

buff1, back_button, page_number, next_button, buff2 = st.columns([3,1,1,1,3])
#page_number.markdown(f"""**{num_of_page}**""")
page_text = page_number.empty()

if 'page' not in st.session_state:
  st.session_state['page'] = num_of_page
  page_text.markdown(f"""{num_of_page}""")
  st.session_state['button_state'] = True
  
if st.session_state.get('next') :
  page_text.empty()
  page_text.markdown(f"""{st.session_state['next']}""")

if st.session_state.get('back') :
  st.write('index di dalam state back')
  st.write(st.session_state['index'])
  page_text.empty()
  page_text.markdown(f"""{st.session_state['back']}""")

back_button.button('back', on_click = back_func, disabled = st.session_state['button_state'])
next_button.button('next', on_click = next_func)
    

st.session_state
#st.write(num_of_item)


#make button use on_click, inside onclick function add session state
