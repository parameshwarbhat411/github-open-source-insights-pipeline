WITH distinct_users AS (
    SELECT DISTINCT stg_gharchive.repo_id, stg_gharchive.repo_name
    FROM {{ ref('stg_gharchive') }}
)

SELECT ROW_NUMBER() OVER() as distinct_repo_id,
    repo_id,
    repo_name
FROM distinct_users
