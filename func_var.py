import pickle
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.neighbors import NearestNeighbors

games = pickle.load(open('games.pkl', 'rb'))
games_sparse = pickle.load(open('urm_sparse.pkl', 'rb'))
knn = pickle.load(open('knn.pkl', 'rb'))
cosine_sim_content = pickle.load(open('cosine_sim_content.pkl', 'rb'))

games_title = games.sort_values(by='title')

# Function to get collaborative filtering similarity for a given game
def get_collaborative_similarities(game_id, k=10):
   game_idx = games[games['app_id'] == game_id].index[0]
   game_vector = games_sparse[game_idx, :]
   distances, indices = knn.kneighbors(game_vector, n_neighbors=k)
   return indices.flatten(), distances.flatten()

# 4. Hybrid Filtering
def hybrid_recommendation(input_game_title, k = 10):
   # Find the game ID for the input title
   input_game_id = games[games['title'] == input_game_title]['app_id'].values[0] 
   input_game_idx = games[games['app_id'] == input_game_id].index[0]
   #games[games['title'].str.contains(input_game_title, case=False)].iloc[0]['app_id']
   
   # Content-based similarity scores
   content_sim_scores = list(enumerate(cosine_sim_content[input_game_idx]))
   
   # Collaborative similarity scores
   collab_indices, collab_distances = get_collaborative_similarities(input_game_id, k+1)
   collab_sim_scores = [(idx, 1 - dist) for idx, dist in zip(collab_indices, collab_distances)]
   
   # Normalize scores
   max_content_score = max([score for _, score in content_sim_scores])
   max_collab_score = max([score for _, score in collab_sim_scores])
   content_sim_scores = [(idx, score / max_content_score) for idx, score in content_sim_scores]
   collab_sim_scores = [(idx, score / max_collab_score) for idx, score in collab_sim_scores]
   
   # Combine scores with a weighted average
   combined_scores = {}
   for idx, score in content_sim_scores:
      combined_scores[idx] = combined_scores.get(idx, 0) + 0.5 * score
   for idx, score in collab_sim_scores:
      combined_scores[idx] = combined_scores.get(idx, 0) + 0.5 * score
   
   # Sort and get top k recommendations
   sorted_games = sorted(combined_scores.items(), key=lambda x: x[1], reverse=True)
   recommended_game_indices = [idx for idx, _ in sorted_games[1:k+1]]
   # Retrieve game titles
   recommended_games = games.iloc[recommended_game_indices].reset_index(drop=True)
   return recommended_games

def sorted_score_df(df):
   df['score'] = df['user_reviews'] * df['positive_ratio']
   df_sorted = df.sort_values('score', ascending=False)
   return df_sorted

def most_popular_games():
   df = games
   n = 12 #number of games
   list = sorted_score_df(df).reset_index(drop = True)
   return list.iloc[0:n]

def genre_filtering(list_genre = []): 
   # memfilter genre 
   df = games
   if len(list_genre) != 0:
      for genre in list_genre:
         genres_games = df[df['genres'].str.contains(genre, case=False)]
         df = genres_games
      filtered_games = sorted_score_df(genres_games).reset_index(drop = True)
   else :
      filtered_games = df.sort_values('title', ascending=True).reset_index(drop = True)
   return filtered_games

def selected_game_details(game_name):
   game_id = games[games['title'] == game_name]['app_id'].values[0] 
   game_idx = games[games['app_id'] == game_id].index[0]
   list_details = games.loc[game_idx].reset_index(drop = True)
   return list_details
   
def unused(cols, recommendations) :
   index=0
   for col in cols:
      data = recommendations[index]
      col.text(data[0])
      col.image(data[1])
      index= index + 1
