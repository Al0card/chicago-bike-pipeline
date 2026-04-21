{{ config(materialized='table') }}
SELECT member_casual, COUNT(*) as trip_count
FROM {{source('bike_data', 'fact_bike_trips')}}
GROUP BY member_casual
