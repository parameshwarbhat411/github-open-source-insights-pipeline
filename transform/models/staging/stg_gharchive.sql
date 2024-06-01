with adjusted_data as (
    select
        CASE
            WHEN type = 'Event' THEN type
            ELSE LEFT(type, LENGTH(type) - 5)
        END as event_type,
        actor.login as 'user',
        repo.id as repo_id,
        repo.name as repo_name,
        created_at as event_date,
        loaded_at as event_loaded_date
    from {{ source('gharchive', 'src_gharchive') }}
    where type LIKE '%Event'
)

select *
from adjusted_data