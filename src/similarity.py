from sklearn.metrics.pairwise import cosine_similarity


def compute_similarity_matrix(feature_matrix):
    """
    Input:
        feature_matrix: sparse matrix (text + numeric)
    
    Output:
        similarity matrix (n_movies x n_movies)
    """
    similarity_matrix = cosine_similarity(feature_matrix)
    return similarity_matrix