from src.load_data import load_data
from src.feature_engineering import build_feature_matrix
from src.similarity import compute_similarity_matrix
from src.recommender import get_recommendations

# ========================
# 1. LOAD DATA
# ========================
df = load_data("D:\\Ds108\\Project\\data")

# 🔥 đảm bảo lowercase để match title
df['title'] = df['title'].str.lower()

# ========================
# 2. BUILD FEATURE
# ========================
feature_matrix, _, _ = build_feature_matrix(df)

# ========================
# 3. COMPUTE SIMILARITY
# ========================
sim_matrix = compute_similarity_matrix(feature_matrix)

# ========================
# 4. TEST RECOMMENDER
# ========================
result = get_recommendations(
    "homecoming: a film by beyoncé",
    df,
    sim_matrix,
    top_n=5,
    min_rating=6
)

print(result)