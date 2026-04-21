{{ config(materialized='table') }}
SELECT trip_hour , COUNT(*) as trip_count
FROM {{source('bike_data', 'fact_bike_trips')}}
GROUP BY trip_hour