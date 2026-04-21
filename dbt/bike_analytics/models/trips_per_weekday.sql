{{ config(materialized='table') }}
SELECT trip_weekday , COUNT(*) as trip_count
FROM {{source('bike_data', 'fact_bike_trips')}}
GROUP BY trip_weekday