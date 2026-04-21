{{ config(materialized='table') }}

SELECT
    f.movie_sk,

    d.title,
    d.genre,
    d.director,

    f.average_rating,
    f.weighted_rating,
    f.num_votes,
    f.log_votes,

    f.rating_diff,
    f.popularity_level

FROM {{ ref('fact_movies') }} f
JOIN {{ ref('dim_movies') }} d
ON f.movie_sk = d.movie_sk