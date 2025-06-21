# core/recommendation/utils.py

import pickle
import pandas as pd

def load_similarity_matrix(path):
    with open(path, "rb") as f:
        return pickle.load(f)

def recommend(movie_title, similarity_df, n=5):
    if movie_title not in similarity_df:
        return []
    sim_scores = similarity_df[movie_title].drop(labels=[movie_title])
    return sim_scores.sort_values(ascending=False).head(n).index.tolist()
