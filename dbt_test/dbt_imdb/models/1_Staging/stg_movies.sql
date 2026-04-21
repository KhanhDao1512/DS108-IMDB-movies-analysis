{{ config(materialized='view') }}

WITH cleaned AS (
    SELECT
        CAST(id AS INT64) AS movie_id,

        LOWER(TRIM(title)) AS title,

        SAFE_CAST(averageRating AS FLOAT64) AS average_rating,
        SAFE_CAST(numVotes AS INT64) AS num_votes,

        COALESCE(LOWER(TRIM(genres)), 'unknown') AS genre,
        COALESCE(LOWER(TRIM(director)), 'unknown') AS director,

        LOWER(TRIM(`cast`)) AS cast_members,

        TRIM(overview) AS overview

    FROM {{ source('raw', 'raw_movies') }}
),

deduplicated AS (
    SELECT *,
        ROW_NUMBER() OVER (
            PARTITION BY movie_id
            ORDER BY num_votes DESC
        ) AS rn
    FROM cleaned
)

SELECT
    movie_id,
    title,
    average_rating,
    num_votes,
    genre,
    director,
    cast_members,
    overview

FROM deduplicated
WHERE rn = 1