# Table name

fact_bike_trips

# Row meaning

One row represents a single bike trip with cleaned and structured features ready for analysis.

# Columns


ride_id
rideable_type
member_casual
started_at
ended_at
trip_year
trip_month
trip_weekday
trip_hour
trip_date
duration_seconds
start_station_id
start_station_name
end_station_id
end_station_name

# Column groups
## Identifiers
ride_id
##Time fields
started_at
ended_at
trip_date
trip_year
trip_month
trip_weekday
trip_hour
## Categorical fields
rideable_type
member_casual
## Location fields
start_station_id
start_station_name
end_station_id
end_station_name
## Numeric measures
duration_seconds
# BigQuery loading inputs

project id: bike-analytics-project-492312
dataset name: bike_data
table name: fact_bike_trips
input file path: path to a single processed file
(e.g. data/processed/trips_clean_202501.csv)
write mode: append (default), with initial load handled when table is empty