WITH distinct_users AS (
    SELECT DISTINCT user
    FROM {{ ref('stg_gharchive') }}
)

SELECT
    ROW_NUMBER() OVER() AS user_id,
    user as user_name
FROM
    distinct_users