import pickle
import streamlit as st
import numpy as np

st.header("Game Recommender System using Machine Learning")
model = pickle.load(open('model.pkl', 'rb'))
#books_name = pickle.load(open('artifacts/books_name.pkl', 'rb'))
games = pickle.load(open('games.pkl', 'rb'))
game_pivot = pickle.load(open('game_pivot.pkl', 'rb'))

def fecth_image(df):
    #list untuk menyimpan url image setiap resep
    game_image = []
    game_name = []
    #game_id =[]
    
    for item in df['title']:
        #mendapatkan index berdasarkan nama resep
        index = df.loc[df['title'] == item].index[0]
        game_name.append(str(item))
        url = df.loc[index,'Header image']
        #url = url[0] 
        #mengecek apakah url image lebih dari 1 item
        #if len(url) > 1:
        #    url = url[0]        #menyimpan url pada list
        game_image.append(str(url))
        
    #recipe_image_string = list(map(str, recipe_image))

    return game_image, game_name

def recommend_books(book_name):
    book_list = []
    book_id = np.where(book_pivot.index == book_name)[0][0]
    distance, suggestion = model.kneighbors(book_pivot.iloc[book_id,:].values.reshape(1,-1), n_neighbors = 11)

    poster_url = fecth_poster(suggestion)

    for i in range(len(suggestion)):
        books = book_pivot.index[suggestion[i]]
        for j in books:
            book_list.append(j)

    return book_list, poster_url

selected_books = st.selectbox(
    "Type or select a book",
    books_name
)

if st.button('Show Recommendation'):
    recommended_books, poster_url = recommend_books(selected_books)
    col1, col2, col3, col4, col5, col6, col7, col8, col9, col10 = st.columns(10)

    with col1:
        st.text(recommended_books[1])
        st.image(poster_url[1])

    with col2:
        st.text(recommended_books[2])
        st.image(poster_url[2])

    with col3:
        st.text(recommended_books[3])
        st.image(poster_url[3])

    with col4:
        st.text(recommended_books[4])
        st.image(poster_url[4])

    with col5:
        st.text(recommended_books[5])
        st.image(poster_url[5]) 

    with col6:
        st.text(recommended_books[6])
        st.image(poster_url[6])

    with col7:
        st.text(recommended_books[7])
        st.image(poster_url[7])
        
    with col8:
        st.text(recommended_books[8])
        st.image(poster_url[8]) 
        
    with col9:
        st.text(recommended_books[9])
        st.image(poster_url[9]) 

    with col10:
        st.text(recommended_books[10])
        st.image(poster_url[10]) 
