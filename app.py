import streamlit as st
import pandas as pd
import numpy as np
import streamlit_antd_components as sac
from func_var import games_title
from func_var import most_popular_games

app_page = st.Page("app.py", title="Halaman Utama", icon="🎮")
game_details_page = st.Page("pages/game_details.py", title="Rekomendasi Game", icon="🎮")
game_directory_page = st.Page("pages/game_directory.py", title="Katalog Game", icon="📃")

#pg = st.navigation([app_page, game_details_page, game_directory_page])
#pg.run()
st.set_page_config(
    page_title="Halaman Utama",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="auto"
)


#with st.sidebar:
#    sac.menu([
#        sac.MenuItem('Halaman Utama', icon='🎮'),
#        sac.MenuItem('Rekomendasi Game', icon='🎮'),
#        sac.MenuItem('Katalog Game', icon='📃'),
#    ], variant='left-bar')

st.title("Aplikasi Rekomendasi Game")

selected_game = st.selectbox(
   "Type or select a game",
   games_title['title'],
   index = None,
   placeholder = "Ketik atau pilih game",
   label_visibility = "collapsed"
)

col1, col2, col3 = st.columns([2, 1, 2])
with col2:
    if st.button('Cari rekomendasi'):
       #selection = str(selected_game)
       st.query_params.game_name = selected_game
       st.switch_page("pages/game_details.py")

st.header("Game Terpopuler")
row1 = st.columns(3)
row2 = st.columns(3)
row3 = st.columns(3)
row4 = st.columns(3)
list_popular = most_popular_games()

index = 0
for col in row1 + row2 + row3 + row4:
    image = list_popular.loc[index,'header_image']
    title = list_popular.loc[index,'title']
    cont = col.container(border = True)
    cont.image(image)
    #cont.text(title)
    if cont.button(title, use_container_width = True):
        st.query_params.game_name = title
        st.switch_page("pages/game_details.py")
    index = index + 1

