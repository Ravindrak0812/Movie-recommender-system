import streamlit as st
import pickle
import pandas as pd
import  requests

def fetch_poster(movie_id):

    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=e78d81bf39c67f0c343db2255067dc3c&language=en-US'.format(movie_id))
    data = response.json()
    print(data)
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
def recommend(movie):
     movie_index = movies[movies['title'] == movie].index[0]
     distances = similarity[movie_index]
     movie_dict = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

     recommend_movie = []
     recommend_movie_posters=[]
     for i in movie_dict:
         movie_id =movies.iloc[i[0]].id
         #fetch poster
         recommend_movie.append(movies.iloc[i[0]].title)
         recommend_movie_posters.append(fetch_poster(movie_id))
     return  recommend_movie,recommend_movie_posters


movie_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movie_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

movie_dict= pickle.load(open('movie_dict.pkl','rb'))
st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Type The Movie Name To Recommend?',
    movies['title'].values)
if st.button('Recommend'):
     name,posters= recommend(selected_movie_name)
     col1, col2, col3,col4,col5 = st.columns(5)

     with col1:
         st.text(name[0])
         st.image(posters[0])

     with col2:
         st.text(name[1])
         st.image(posters[1])
     with col3:
         st.text(name[2])
         st.image(posters[2])

     with col4:
         st.text(name[3])
         st.image(posters[3])
     with col5:
         st.text(name[4])
         st.image(posters[4])