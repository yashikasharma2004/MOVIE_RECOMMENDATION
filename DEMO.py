import streamlit as st
import pickle
import pandas as pd

# ---- Recommend Function ----
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for idx, _ in movies_list:
        row = movies.iloc[idx]
        recommended_movies.append(row['title'])

    return recommended_movies

# ---- Load Data ----
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# ---- Streamlit UI ----
st.title('🎬 Movie Recommender System (Without Posters)')

selected_movie_name = st.selectbox(
    'Which movies would you like to see today?',
    movies['title'].values
)

if st.button('RECOMMEND'):
    names = recommend(selected_movie_name)
    cols = st.columns(5)
    for i, col in enumerate(cols):
        with col:
            st.text(names[i])
