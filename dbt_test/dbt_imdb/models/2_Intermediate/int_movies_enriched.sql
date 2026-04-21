{{ config(materialized='view') }}

WITH base AS (
    SELECT *
    FROM {{ ref('stg_movies') }}
),

stats AS (
    SELECT
        AVG(average_rating) AS avg_rating,
        APPROX_QUANTILES(num_votes, 100)[OFFSET(80)] AS dynamic_min_votes
    FROM base
)

SELECT
    b.movie_id,
    b.title,
    b.genre,
    b.director,
    b.cast_members,
    b.overview,

    b.average_rating,
    b.num_votes,

    -- global stats
    s.avg_rating AS global_avg_rating,
    s.dynamic_min_votes AS min_votes,

    -- 🔥 Insight 1: deviation
    (b.average_rating - s.avg_rating) AS rating_diff,

    -- 🔥 Insight 2: popularity bucket
    CASE
        WHEN b.num_votes >= s.dynamic_min_votes THEN 'high'
        WHEN b.num_votes >= s.dynamic_min_votes * 0.5 THEN 'medium'
        ELSE 'low'
    END AS popularity_level

FROM base b
CROSS JOIN stats s