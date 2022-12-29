import streamlit as st
import pickle
import pandas as pd
import numpy as np
import requests


# def fetch_poster(movie_id):
#     response = requests.get(
#     'https://api.themoviedb.org/3/movie/{}?api_key=512ba153af55936f686becbd47370b79&language=en-US'.format(movie_id))
#     data = response.json()
#     return "http://image.tmdb.org/t/p/w500/" + data('poster_path')


def Recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    dist = similar[movie_index]
    movies_list = sorted(list(enumerate(dist)),
                        reverse=True, key=lambda x: x[1])[1:6]
    recommende_movie = []
    # recommende_movie_posters = []

    for i in movies_list:
        movie_id = i[0]

        recommende_movie.append(movies.iloc[i[0]].title)
        # recommende_movie_posters.append(fetch_poster(movie_id))
    return recommende_movie


movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similar = pickle.load(open('similar.pkl', 'rb'))

st.title('Recommender System')
selected_movie_name = st.selectbox(
    'Which movie you watched recently?',
    movies['title'].values)

if st.button('Recommend'):
    recommendation=Recommend(selected_movie_name)
    for i in recommendation:
        st.write(i)
# if st.button('Recommend'):
#     recommende_movie,  = Recommend(
#         selected_movie_name)
#     col1, col2, col3, col4, col5 = st.beta_columns(5)
#     with col1:
#         st.text(recommended_movie_names[0])
#         st.image(recommended_movie_posters[0])
#     with col2:
#         st.text(recommended_movie_names[1])
#         st.image(recommended_movie_posters[1])

#     with col3:
#         st.text(recommended_movie_names[2])
#         st.image(recommended_movie_posters[2])
#     with col4:
#         st.text(recommended_movie_names[3])
#         st.image(recommended_movie_posters[3])
#     with col5:
#         st.text(recommended_movie_names[4])
#         st.image(recommended_movie_posters[4])
