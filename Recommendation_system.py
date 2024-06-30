import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors

movies = pd.read_csv('movies.csv')
ratings = pd.read_csv('ratings.csv')

final_dataset = pd.merge(ratings, movies, on='movieId')

user_item_matrix = final_dataset.pivot_table(index='userId', columns='title', values='rating', fill_value=0)

sparsity = 1.0 - (np.count_nonzero(user_item_matrix) / float(user_item_matrix.size))
print(f'Sparsity: {sparsity:.2f}')

csr_data = csr_matrix(user_item_matrix.values)

knn = NearestNeighbors(metric='cosine', algorithm='brute', n_neighbors=10, n_jobs=-1)

knn.fit(csr_data)

def get_movie_recommendation(movie_name, matrix, knn_model, movies_df, n_recs=4):
  
    movie_list = movies_df[movies_df['title'].str.lower().str.contains(movie_name.lower())]
    
    if not movie_list.empty:
        movie_idx = movie_list.index[0]
        
        distances, indices = knn_model.kneighbors(matrix[movie_idx], n_neighbors=n_recs+1)
        
        rec_movie_indices = indices.squeeze()[1:]
        
        recommend_frame = []
        for idx in rec_movie_indices:
            title = movies_df.iloc[idx]['title']
            distance = distances.squeeze()[idx]
            recommend_frame.append({'Title': title, 'Distance': distance})
        
        return pd.DataFrame(recommend_frame, columns=['Title', 'Distance'])
    else:
        return f"No movies found matching '{movie_name}'."

if __name__ == "__main__":
    movie_name = input("Enter the movie name:")
    recommendations = get_movie_recommendation(movie_name, csr_data, knn, movies)
    print(f"Recommendations for '{movie_name}':")
    print(recommendations)
