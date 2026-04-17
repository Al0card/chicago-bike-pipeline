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

# 🐳 Docker Usage
Here’s a clean, concise README section you can drop directly into your project:

---

### Prerequisites

* Docker installed
* Google Cloud SDK authenticated locally:

  ```bash
  gcloud auth application-default login
  ```
* Your ADC file exists at:

  ```
  ~/.config/gcloud/application_default_credentials.json
  ```
* A `data/` folder in the project containing raw CSV files

---

### Build the image

```bash
docker build -t my-pipeline .
```

---

### Run the pipeline

```bash
docker run \
-v "$(pwd)/data:/usr/local/pipeline/data" \
-v "/home/ely0rda/.config/gcloud/application_default_credentials.json:/usr/local/pipeline/credentials/application_default_credentials.json" \
-e GOOGLE_APPLICATION_CREDENTIALS="/usr/local/pipeline/credentials/application_default_credentials.json" \
-e GOOGLE_CLOUD_PROJECT="bike-analytics-project-492312" \
my-pipeline
```

---

### 📦 Volume mounts explained

#### 1. `data/` mount

```bash
-v "$(pwd)/data:/usr/local/pipeline/data"
```

* Shares your local `data/` folder with the container
* Input CSV files are read from here
* Processed files are also written here

---

#### 2. ADC credentials file

```bash
-v "/home/ely0rda/.config/gcloud/application_default_credentials.json:/usr/local/pipeline/credentials/application_default_credentials.json"
```

* Mounts your local Google Cloud credentials into the container
* Required for authentication with BigQuery

---

### 🔐 Environment variables

#### `GOOGLE_APPLICATION_CREDENTIALS`

```bash
-e GOOGLE_APPLICATION_CREDENTIALS="/usr/local/pipeline/credentials/application_default_credentials.json"
```

* Tells the Google SDK where to find your credentials file inside the container

---

#### `GOOGLE_CLOUD_PROJECT`

```bash
-e GOOGLE_CLOUD_PROJECT="bike-analytics-project-492312"
```

* Specifies which GCP project BigQuery should use

---

### ▶️ Expected behavior

When the container runs:

1. Reads raw CSV files from `/data`
2. Processes and cleans each file
3. Saves processed files back to `/data`
4. Loads the cleaned data into BigQuery

You should see logs like:

```
Processing 202503-divvy-tripdata.csv
file: trips_clean_202503.csv saved
trips_clean_202503.csv loaded successfully.
All files processed
```

---
