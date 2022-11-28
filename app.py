import pickle,requests
from turtle import Turtle, pos
import streamlit as st
with open('static/style.css') as styles:
    st.markdown(f"<style>{styles.read()}</style>",unsafe_allow_html=True)
movies = pickle.load(open('movie_list.pkl','rb'))
cosine_sim = pickle.load(open('similarity.pkl','rb'))

def fetch_poster(movie_id):
    url="https://api.themoviedb.org/3/movie/{}?api_key=e901ee4b35fb916917a7b2a5421d3249&language=en-US".format(movie_id)
    data=requests.get(url)
    data=data.json()
    poster_path=data['poster_path']
    full_path="https://image.tmdb.org/t/p/w500/"+poster_path
    return full_path



def recommend(movie):
    idx=movies[movies['title']==movie].index[0]
    sim_scores=sorted(list(enumerate(cosine_sim[idx])),key=lambda x:x[1],reverse=True)
    recommend_movies_names=[]
    recommend_movies_posters=[]
    for i in sim_scores[1:7]:
        movie_id=movies.iloc[i[0]].id
        recommend_movies_posters.append(fetch_poster(movie_id))
        recommend_movies_names.append(movies.iloc[i[0]].title)

    return recommend_movies_posters,recommend_movies_names


heading="""<style>color:white</style> """
st.markdown("<h1 style='text-align: center;color: darkred; font-size: 50px;font-family: cursive;'>Movie Recommender System</h1>",unsafe_allow_html=True)
movie_list=movies['title'].values
selected_movie=st.selectbox("Type or select a movie from dropdown",movie_list)
st.markdown("<style>.stTextInput > label {color:darkred;} </style>",unsafe_allow_html=True)
# st.markdown("")
hide_menu_style="""<style>
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
</style>"""

st.markdown(hide_menu_style,unsafe_allow_html=True)
st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://editor.analyticsvidhya.com/uploads/76889recommender-system-for-movie-recommendation.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

if st.button("Show Recommendation"):
    recommended_movie_posters,recommended_movie_names=recommend(selected_movie)
    col1, col2, col3, col4, col5,col6 = st.columns(6)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4]) 
    with col6:
        st.text(recommended_movie_names[5])
        st.image(recommended_movie_posters[5])





