import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

class UserBasedCF:
    def __init__(self):
        self.user_similarity = None
        self.ratings_matrix = None
        
    def fit(self, ratings_df):
        # Create user-item matrix
        self.ratings_matrix = ratings_df.pivot_table(
            index='user_id', 
            columns='movie_id', 
            values='rating'
        ).fillna(0)
        
        # Compute user similarity
        self.user_similarity = cosine_similarity(self.ratings_matrix)
        
    def predict(self, user_id, movie_id, k=5):
        if user_id not in self.ratings_matrix.index or movie_id not in self.ratings_matrix.columns:
            return 0  # or handle missing data
        
        # Get similar users
        user_idx = self.ratings_matrix.index.get_loc(user_id)
        similar_users = np.argsort(-self.user_similarity[user_idx])[1:k+1]  # exclude self
        
        # Calculate weighted average of ratings from similar users
        weighted_sum = 0
        similarity_sum = 0
        
        for sim_user_idx in similar_users:
            sim_user_id = self.ratings_matrix.index[sim_user_idx]
            rating = self.ratings_matrix.loc[sim_user_id, movie_id]
            if rating > 0:
                similarity = self.user_similarity[user_idx, sim_user_idx]
                weighted_sum += similarity * rating
                similarity_sum += similarity
                
        if similarity_sum == 0:
            return 0
            
        return weighted_sum / similarity_sum
