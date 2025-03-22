






#working code I
import streamlit as st
import pickle
import pandas as pd

# ✅ Function to get Google Image search link
def get_google_image_url(movie_name):
        return f"https://www.google.com/search?tbm=isch&q={movie_name.replace(' ', '+')}+movie+poster"

# ✅ Function to Recommend Movies
def recommend(movie):
    try:
        movie_index = movies[movies['title'] == movie].index[0]
        distances = similarity[movie_index]
        movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

        recommended_movies = []
        recommended_movies_posters = []
        
        for i in movies_list:
             movie_name = movies.iloc[i[0]].title
             google_image_url = get_google_image_url(movie_name)  # 🔍 Link to Google Images
            
             recommended_movies.append(movie_name)
             recommended_movies_posters.append(google_image_url)
        
        return recommended_movies, recommended_movies_posters

    except Exception as e:
         print("❌ Recommendation Error:", e)
         return [], []

 # ✅ Load Movie Data
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

 # ✅ Streamlit UI
st.header('🎬 Movie Recommender System')
st.subheader("Find your next favorite movie! 🍿")

selected_movie_name = st.selectbox("Choose a movie:", movies['title'].values)

if st.button('Recommend'):
    names, google_links = recommend(selected_movie_name)

    if not names:
         st.error("No recommendations found. Please try another movie.")
    else:
        cols = st.columns(5)
        for idx, col in enumerate(cols):
             with col:
                 st.text(names[idx])
                 st.markdown(f"[🔍 View Poster]({google_links[idx]})", unsafe_allow_html=True)
