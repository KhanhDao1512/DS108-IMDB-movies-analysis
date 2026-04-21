{{ config(materialized='table') }}

SELECT
    FARM_FINGERPRINT(CAST(movie_id AS STRING)) AS movie_sk,  -- FIX

    movie_id,
    title,
    genre,
    director,
    cast_members,
    overview

FROM {{ ref('stg_movies') }}