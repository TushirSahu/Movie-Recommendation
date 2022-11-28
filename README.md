# Movie-Recommendation
A content-based recommender system that recommends movies similar to the movie the user likes and analyses the sentiments of the reviews given by the user.
The movies are recommended based on the content of the movie you entered or selected. The main parameters that are considered for the recommendations are the genre, director, and top 3 casts. The details of the movies, such as title, genre, runtime, rating, poster, casts, etc., are fetched from TMDB.
## Dataset:
Basilcally used content-based filtering from dataset from tmdb site.Link for the dataset:https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata.
![Screenshot from 2022-11-28 17-03-27](https://user-images.githubusercontent.com/96677478/204267831-cd2548ce-4373-465c-8c0b-f790a4c9589b.png)

## Methods Used:
For converting the description I used the Word Embeddings or Word vectorizationvectorization with help of ConterVectorizer of sklearn.Used the cosine similarity for getting the relationship between movies based on the description of the movies.Then apllied the streamlit for deploying it on webpage.
## Poster Fetching:
I used API of TMDB site for the poster fetching and then used the streamlit python library for the interface design.I tried some css with streamlit library but didn't go so well.I hope so improving the interface in the near future.
 
