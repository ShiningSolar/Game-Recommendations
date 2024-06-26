import streamlit as st
import streamlit_antd_components as sac
from func_var import hybrid_recommendation
from func_var import selected_game_details
from streamlit_image_select import image_select

st.set_page_config(
    page_title="Rekomendasi Game",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="auto"
)

def button_details(popover, title):
    if popover.button('view more', key = title, use_container_width = True):
        st.query_params.game_name = title
        st.switch_page("pages/game_details.py")

def detail_selected_game(game_name, details):
    genres = details.loc['genres']
    tanggal = str(details.loc['date_release'])
    website = details.loc['website']
    screenshots = details.loc['screenshots']
    ss_lenght = len(screenshots)
    con = st.container(border = True)
    cols_con = con.columns([3, 2])
    with cols_con[0]:
        with st.container(border = True):
            placeholder_screenshot = st.empty()
            placeholder_screenshot.image(screenshots[0], use_column_width = True)
        with st.container(height=500, border = True):
            img = image_select(label = "screenshots", images = screenshots)
    with cols_con[1].container(border=True):
        st.image(details.loc['header_image'], use_column_width = True)
        st.header(details.loc['title'])
        sac.divider(label='Genre', align='center', color='gray')
        sac.buttons(genres, label='', index=None, align='center', size='sm', radius='lg', gap='sm', variant='filled', color='dark', use_container_width=True)
        sac.divider(label='Tanggal Rilis', align='center', color='gray')    
        sac.tags(genres, align='center', size='md')

def view(game_name):
    recommendations = hybrid_recommendation(game_name)
    data = recommendations

    details = selected_game_details(game_name)
    detail_selected_game(game_name, details)
    
    st.header("Recommendations games")
    row1 = st.columns(2)
    row2 = st.columns(2)
    row3 = st.columns(2)
    row4 = st.columns(2)
    row5 = st.columns(2)
    
    index = 0
    for col in row1 + row2 + row3 + row4 + row5:
        cont = col.container(border = True)
        cont.image(data.loc[index,'header_image'], use_column_width = True)
        title = data.loc[index,'title']
        tanggal = str(data.loc[index, 'date_release'])
        website = data.loc[index, 'website']
        popover = cont.popover(title, use_container_width = True)
        cols1 = popover.columns([1, 3])
        cols2 = popover.columns([1, 3])
        cols1[0].markdown('**Tanggal rilis :**')
        cols1[1].markdown(tanggal[:10])
        cols2[0].markdown('**Genre :**')
        cols2[1].markdown(data.loc[index, 'genres'])
        if website != 'Unknown':
            cols3 = popover.columns([1, 3])
            cols3[0].markdown('**Website :**')
            cols3[1].page_link(website, label="go to website", icon="🌎")
        index = index + 1


game_name = ""

if "game_name" in st.query_params:
    game_name = st.query_params.game_name
    st.session_state['saved_name'] = game_name
    view(game_name)
else:
    if 'saved_name' in st.session_state:
        game_name = st.session_state['saved_name']
        view(game_name)
    else:
        with st.container(border = True):
            st.header('🔴 PILIH GAME TERLEBIH DAHULU 🔴')
            st.page_link("🏠_Beranda.py", label="Beranda", icon="🏠", use_container_width = True)
            st.page_link("pages\📃_Katalog_Game.py", label="Katalog Game", icon="📃", use_container_width = True)