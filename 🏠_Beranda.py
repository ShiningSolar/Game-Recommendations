import streamlit as st
import pandas as pd
import numpy as np
import streamlit_antd_components as sac
from func_var import games_title
from func_var import most_popular_games

st.set_page_config(
    page_title="Beranda",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="auto"
)

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
    if cont.button(title, use_container_width = True):
        st.query_params.game_name = title
        st.switch_page("pages\🎮_Rekomendasi_Game.py")
    index = index + 1

