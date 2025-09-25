import streamlit as st
import pickle
import pandas as pd

# Load pickles (instant)
movies = pickle.load(open("movies.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))

st.title("🎬 Movie Recommender System")

# Movie selector
movie_list = movies["title"].values
selected_movie = st.selectbox("Choose a movie", movie_list)

def recommend(movie):
    index = movies[movies["title"] == movie].index[0]
    distances = similarity[index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    return [movies.iloc[i[0]].title for i in movies_list]

if st.button("Recommend"):
    recommendations = recommend(selected_movie)
    st.write("### Recommended Movies:")
    for rec in recommendations:
        st.write(f"- {rec}")
