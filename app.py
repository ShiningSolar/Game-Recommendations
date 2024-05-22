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
item_similarity = pickle.load(open('item_similarity.pkl', 'rb'))

distances, indices = model.kneighbors(game_sparse.T, n_neighbors=game_sparse.shape[1])

def fecth_image(df):
    #list untuk menyimpan url image setiap resep
    game_image = []
    game_name = []
    for item in df:
        #mendapatkan index berdasarkan nama resep
        index = games.loc[games['app_id'] == item].index[0]
        title = games.loc[games['app_id'] == item]['title'].values[0]
        game_name.append(str(title))
        url = games.loc[index,'Header image']
        game_image.append(str(url))
    return game_image, game_name
    
def recommend_games_based_on_item(item_name, indices, item_similarity_df, top_n=5):
    game_id = games[games['title'] == item_name]['app_id'].values[0]
    similar_indices = indices[game_id][1:top_n+1]
    similar_items = item_similarity_df.columns[similar_indices]
    game_image, game_name = fecth_image(similar_items)
    return similar_items, game_image, game_name
'''
def generate_knn_recommendations(item_name, df, knn_model, n_neighbors=5):
    item_id = df[df['title'] == item_name]['app_id'].values[0]
    item_index = df[df['app_id'] == item_id].index[0]
    distances, indices = knn_model.kneighbors(df[item_index], n_neighbors=n_neighbors + 1)
    similar_items = df.iloc[indices[0][1:]]  # Menghapus item itu sendiri dari hasil
    game_image, game_name = fecth_image(similar_items)
    return similar_items, game_image, game_name
'''
selected_game = st.selectbox(
    "Type or select a game",
    games['title']
)

if st.button('Show Recommendation'):
    #recommendations, game_image, game_name = generate_knn_recommendations(selected_game, games, model)
    recommendations_game, game_image, game_name = recommend_games_based_on_item(selected_game, indices, item_similarity)
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
