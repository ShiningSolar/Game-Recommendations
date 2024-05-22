import pickle
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.neighbors import NearestNeighbors

st.header("Game Recommender System using Machine Learning")
model = pickle.load(open('model.pkl', 'rb'))
#books_name = pickle.load(open('artifacts/books_name.pkl', 'rb'))
games = pickle.load(open('games.pkl', 'rb'))
game_sparse = pickle.load(open('game_sparse.pkl', 'rb'))

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
        game_image.append(str(url))
    return game_image, game_name

def generate_knn_recommendations(item_name, df, knn_model, n_neighbors=5):
    item_id = df[df['title'] == item_name]['app_id'].values[0]
    item_index = game_sparse[game_sparse['app_id'] == item_id].index[0]
    distances, indices = knn_model.kneighbors(game_sparse[item_index], n_neighbors=n_neighbors + 1)
    similar_items = df.iloc[indices[0][1:]]  # Menghapus item itu sendiri dari hasil
    game_image, game_name = fecth_image(similar_items)
    return similar_items, game_image, game_name

selected_game = st.selectbox(
    "Type or select a book",
    games['title']
)

if st.button('Show Recommendation'):
    recommendations, game_image, game_name = generate_knn_recommendations(selected_game, games, model)
    
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(game_name[0])
        st.image(game_image[0])

    with col2:
        st.text(game_name[1])
        st.image(game_image[1])

    with col3:
        st.text(game_name[2])
        st.image(game_image[2])

    with col4:
        st.text(game_name[3])
        st.image(game_image[3])

    with col5:
        st.text(game_name[4])
        st.image(game_image[4]) 
