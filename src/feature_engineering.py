import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import StandardScaler
from scipy.sparse import hstack


# ========================
# 1. BUILD TEXT FEATURE
# ========================
def build_text_feature(df):
    df = df.copy()

    # clean nhẹ
    df['genre'] = df['genre'].fillna('')
    df['director'] = df['director'].fillna('')

    # 🔥 combine feature (có weighting nhẹ)
    df['content'] = (
        df['genre'] * 2 + " " +   # ưu tiên genre
        df['director']
    )

    return df


# ========================
# 2. TF-IDF VECTORIZE
# ========================
def tfidf_vectorize(df, max_features=5000):
    tfidf = TfidfVectorizer(
        stop_words='english',
        max_features=max_features,
        ngram_range=(1, 2)  # 🔥 bắt được cụm từ (e.g. "science fiction")
    )

    text_matrix = tfidf.fit_transform(df['content'])

    return text_matrix, tfidf


# ========================
# 3. NUMERICAL FEATURES
# ========================
def scale_numerical(df):
    df = df.copy()

    features = df[['weighted_rating', 'log_votes', 'rating_diff']]

    scaler = StandardScaler()
    num_matrix = scaler.fit_transform(features)

    return num_matrix, scaler


# ========================
# 4. OPTIONAL: POPULARITY ENCODE
# ========================
def encode_popularity(df):
    mapping = {'low': 0, 'medium': 1, 'high': 2}
    return df['popularity_level'].map(mapping).values.reshape(-1, 1)


# ========================
# 5. COMBINE FEATURES
# ========================
def combine_features(
    text_matrix,
    num_matrix,
    popularity_matrix=None,
    text_weight=0.7,
    num_weight=0.3
):
    # 🔥 scale importance
    text_matrix = text_matrix * text_weight
    num_matrix = num_matrix * num_weight

    matrices = [text_matrix, num_matrix]

    if popularity_matrix is not None:
        matrices.append(popularity_matrix)

    combined = hstack(matrices)

    return combined


# ========================
# 6. FULL PIPELINE
# ========================
def build_feature_matrix(df):
    df = build_text_feature(df)

    text_matrix, tfidf = tfidf_vectorize(df)
    num_matrix, scaler = scale_numerical(df)
    pop_matrix = encode_popularity(df)

    combined = combine_features(
        text_matrix,
        num_matrix,
        pop_matrix
    )

    return combined, tfidf, scaler