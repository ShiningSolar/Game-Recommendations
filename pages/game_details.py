import streamlit as st
#from app import selection
from func_var import hybrid_recommendation
from func_var import selected_game_details

game_name = st.query_params.game_name
recommendations = hybrid_recommendation(game_name)
data = recommendations

details = selected_game_details(game_name)
#st.dataframe(details)
con = st.container(border = True)
con.image(details.loc['header_image'], use_column_width = True)
con.title(details.loc['title'])
con.text(details.loc['date_release'])
with con.popover("About game", use_container_width  = True):
  st.write(details.loc['about'])
con.text(details.loc['genres'])

st.header("Recommendations games")
row1 = st.columns(2)
row2 = st.columns(2)
row3 = st.columns(2)
row4 = st.columns(2)
row5 = st.columns(2)

index = 0
for col in row1 + row2 + row3 + row4 + row5:
  cont = col.container(border = True)
  cont.image(data.loc[index,'header_image'])
  cont.text(data.loc[index,'title'])
  with cont.popover("details", use_container_width = True):
    st.text("test")
  index = index + 1
