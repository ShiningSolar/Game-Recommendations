import pickle
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.neighbors import NearestNeighbors


st.header("Game Recommender System using Machine Learning")
#model = pickle.load(open('model.pkl', 'rb'))
#books_name = pickle.load(open('artifacts/books_name.pkl', 'rb'))
games = pickle.load(open('games.pkl', 'rb'))
#game_sparse = pickle.load(open('game_sparse.pkl', 'rb'))
similarity_score = pickle.load(open('similarity_score.pkl', 'rb'))
   
def recommend(game_name):
    
    game_id = games[games['title'] == game_name]['app_id'].values[0]
    game_idx = games[games['app_id'] == game_id].index[0]
    
    # Sorts the similarities for the book_name in descending order
    similar_games = sorted(list(enumerate(similarity_score[game_idx])),key=lambda x:x[1], reverse=True)[1:6]
    
    # To return result in list format
    data = []
    
    for index,similarity in similar_games:
        item = []
        # Get the book details by index
        temp_df = games.loc[index]

        # Only add the title, author, and image-url to the result
        item.append(temp_df['title'])
        item.append(temp_df['header_image'])
        
        data.append(item)
    return data

selected_game = st.selectbox(
    "Type or select a game",
    games['title']
)

if st.button('Show Recommendation'):
    recommendations = recommend(selected_game)
    #col1, col2, col3, col4, col5 = st.columns(5)
    cols = st.columns(5)
    index=0
    for col in cols:
        data = recommendations[index]
        col.text(data[0])
        col.image(data[1])
                  
    '''
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
    '''
