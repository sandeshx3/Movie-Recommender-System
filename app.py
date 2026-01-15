# app.py
import streamlit as st
import pickle
import pandas as pd
import requests
import os
import re
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
API_KEY = os.environ.get("TMDB_API_KEY")

# ------------------ Fetch Poster ------------------
def fetch_poster(movie_id):
    """
    Fetch movie poster from TMDb API
    """
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}"
    response = requests.get(url)
    data = response.json()
    
    poster_path = data.get("poster_path")
    if poster_path:
        return f"https://image.tmdb.org/t/p/w500{poster_path}"
    return "https://via.placeholder.com/500x750?text=No+Image"

# ------------------ Recommend Function ------------------
def recommend(movie):
    """
    Recommend top 5 similar movies
    """
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]  # Skip the first one (same movie)

    recommended_movies = []
    recommended_movies_posters = []

    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id  # TMDB movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_movies_posters

# ------------------ Load Data ------------------
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

# ------------------ Streamlit UI ------------------
st.set_page_config(page_title="Movie Recommender", layout="wide")
st.title("🎬 Movie Recommender System")

# Escape movie titles to prevent regex issues on mobile
escaped_movie_titles = [re.escape(title) for title in movies['title'].values]

# Dropdown selection (safe for all devices)
selected_movie_name = st.selectbox(
    "Select a movie",
    escaped_movie_titles
)

# Unescape for recommendation logic
selected_movie_name = re.sub(r"\\(.)", r"\1", selected_movie_name)

# Recommend button
if st.button("Recommend"):
    names, posters = recommend(selected_movie_name)

    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.text(names[i])
            st.image(posters[i])
