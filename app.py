import streamlit as st
import pickle
import pandas as pd
import requests




def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?language=en-US".format(movie_id)

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJkY2Y0MzA2YjYzZTU1MjYwMDcxMTViYTc3NjExNWUyZCIsIm5iZiI6MTcxOTY0MjYyNi4xNjg0MTQsInN1YiI6IjY2N2ZhN2IwODNhOTBmYzhjYjY3ZTA4MiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.wFeeAAXz82patfSDqtu-zGFZB9vqECt_hC5tu88cRzM"
    }
    response = requests.get(url , headers=headers)
    data = response.json()
    print(data)
    return  "https://image.tmdb.org/t/p/original/" + data['poster_path']


def recommend(movieTitle):
    movie_index = movies[movies['title'] == movieTitle].index[0]
    distance = similarity[movie_index]
    movies_list = sorted(list(enumerate(distance)),reverse = True , key= lambda x : x[1])[1:6]

    recommended_movies = []
    recommeded_movies_poster = []
    for i in movies_list:
        movie_id =movies.iloc[i[0]].movie_id
        # Fetch poster from api
        recommeded_movies_poster.append(fetch_poster(movie_id))
        # Fetch movie name 
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies , recommeded_movies_poster        

movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recomendation System')

selectedMovieName = st.selectbox('Choose your genre',
                       movies['title'].values)

if st.button('Recommend'):
    names , poster = recommend(selectedMovieName)
    col1 , col2 , col3 , col4 , col5= st.columns(5)
    with col1:
        st.text(names[0])
        st.image(poster[0])
    with col2:
        st.text(names[1])
        st.image(poster[1])
    with col3:
        st.text(names[2])
        st.image(poster[2])
    with col4:
        st.text(names[3])
        st.image(poster[3])
    with col5:
        st.text(names[4])
        st.image(poster[4])    
