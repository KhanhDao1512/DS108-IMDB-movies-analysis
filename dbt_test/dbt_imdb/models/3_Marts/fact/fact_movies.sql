{{ config(materialized='table') }}

SELECT
    d.movie_sk,

    i.average_rating,
    i.num_votes,

    i.global_avg_rating,
    i.min_votes,

    -- 🎯 Core metric
    (i.num_votes / (i.num_votes + i.min_votes)) * i.average_rating +
    (i.min_votes / (i.num_votes + i.min_votes)) * i.global_avg_rating
    AS weighted_rating,

    -- 🔥 Insight 1: deviation
    (i.average_rating - i.global_avg_rating) AS rating_diff,

    -- 🔥 Insight 2: popularity bucket
    CASE
        WHEN i.num_votes >= i.min_votes THEN 'high'
        WHEN i.num_votes >= i.min_votes * 0.5 THEN 'medium'
        ELSE 'low'
    END AS popularity_level,

    -- 🔥 Insight 3: log scale
    LOG10(i.num_votes + 1) AS log_votes

FROM {{ ref('int_movies_enriched') }} i
JOIN {{ ref('dim_movies') }} d
    ON i.movie_id = d.movie_id