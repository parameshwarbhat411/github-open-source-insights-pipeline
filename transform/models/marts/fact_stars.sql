SELECT
    event_date::DATE AS date,
    dr.distinct_repo_id,
    du.user_id
FROM
    {{ ref('stg_gharchive') }} as stg
JOIN
    {{ ref('dim_repos') }} dr
ON
    stg.repo_name = dr.repo_name
JOIN
    {{ ref('dim_users') }} du
ON
    stg.user = du.user_name
WHERE
    stg.event_type = 'Watch'