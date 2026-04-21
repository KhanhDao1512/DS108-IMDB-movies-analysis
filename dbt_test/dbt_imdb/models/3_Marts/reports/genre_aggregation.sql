{{ config(materialized='view') }}

SELECT
    genre,
    COUNT(*) AS movie_count,
    AVG(weighted_rating) AS avg_rating,
    AVG(num_votes) AS avg_votes
FROM {{ ref('mart_movies') }}
GROUP BY genre