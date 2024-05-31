import streamlit as st
#from app import selection
from func_var import hybrid_recommendation
from func_var import selected_game_details

st.set_page_config(
    page_title="Game Details",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="auto"
)
def button_details(popover, title):
    if popover.button('view more', key = title, use_container_width = True):
        st.query_params.game_name = title
        st.switch_page("pages/game_details.py")
    

@st.cache_data
def view(game_name):
    recommendations = hybrid_recommendation(game_name)
    data = recommendations
    
    details = selected_game_details(game_name)
    #st.dataframe(details)
    tanggal = str(details.loc['date_release'])
    website = details.loc['website']
    screenshots = details.loc['screenshots']
    con = st.container(border = True)
    con.image(details.loc['header_image'], use_column_width = True)
    con.title(details.loc['title'])
    cols1 = con.columns([1, 3])
    cols2 = con.columns([1, 3])
    cols1[0].markdown('**Tanggal rilis :**')
    cols1[1].markdown(tanggal[:10])
    cols2[0].markdown('**Genre :**')
    cols2[1].markdown(details.loc['genres'])
    if website != 'Unknown':
        cols3 = con.columns([1, 3])
        cols3[0].markdown('**Website :**')
        cols3[1].page_link(website, label="go to website", icon="🌎")
    with con.popover("About game", use_container_width  = True):
        st.write(details.loc['about'])
    #con.markdown('**Screenshots :**')
    with con.popover("Screenshots", use_container_width  = True):
        st.write(screenshots)
    #cols4 = con.columns([1, 1])
    #con.markdown(screenshots)
    #cols4[0].image(screenshots[0])
    #cols4[1].image(screenshots[1])
    
    
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
        #cont.text(data.loc[index,'title'])
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
        #button_details(popover, title)
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
            st.page_link("app.py", label="Halaman Utama", icon="🏠", use_container_width = True)
            st.page_link("pages/game_directory.py", label="Daftar Game", icon="📃", use_container_width = True)

