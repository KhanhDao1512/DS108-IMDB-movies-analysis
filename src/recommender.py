import pandas as pd
def get_recommendations(
    title,
    df,
    similarity_matrix,
    top_n=5,
    min_rating=0
):

    title = title.lower()

    idx_list = df.index[df['title'] == title].tolist()
    if not idx_list:
        return f"Movie '{title}' not found."

    idx = idx_list[0]

    scores = list(enumerate(similarity_matrix[idx]))

    # convert sang DataFrame
    sim_df = pd.DataFrame(scores, columns=['index', 'similarity'])

    sim_df = sim_df.sort_values(by='similarity', ascending=False)

    # bỏ chính nó
    sim_df = sim_df.iloc[1:]

    results = df.iloc[sim_df['index']].copy()
    results['similarity'] = sim_df['similarity'].values

    # filter quality
    if min_rating > 0:
        results = results[results['weighted_rating'] >= min_rating]

    # 🔥 HYBRID SCORE (FIX)
    results['final_score'] = (
        0.6 * results['similarity'] +
        0.3 * results['weighted_rating'] +
        0.1 * results['rating_diff']
    )

    results = results.sort_values(by='final_score', ascending=False)

    return results[['title', 'similarity', 'weighted_rating', 'final_score']].head(top_n)