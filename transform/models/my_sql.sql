with source_data as (
    select * from {{ source('gharchive','src_gharchive')}}
)

select *
from source_data