import sys
from google.cloud import bigquery
import os.path
from pathlib import Path
from google.cloud.exceptions import NotFound
import re

def table_exists(client, table_id):
    try:
        client.get_table(table_id)
        return True
    except NotFound:
        return False

def create_table(client, table_id):
    schema = [
        bigquery.SchemaField("ride_id", "STRING"),
        bigquery.SchemaField("rideable_type", "STRING"),
        bigquery.SchemaField("started_at", "TIMESTAMP"),
        bigquery.SchemaField("ended_at", "TIMESTAMP"),
        bigquery.SchemaField("start_station_name", "STRING"),
        bigquery.SchemaField("start_station_id", "STRING"),
        bigquery.SchemaField("end_station_name", "STRING"),
        bigquery.SchemaField("end_station_id", "STRING"),
        bigquery.SchemaField("member_casual", "STRING"),
        bigquery.SchemaField("duration_seconds", "FLOAT"),
        bigquery.SchemaField("trip_date", "DATE"),
        bigquery.SchemaField("trip_year", "INTEGER"),
        bigquery.SchemaField("trip_month", "INTEGER"),
        bigquery.SchemaField("trip_weekday", "STRING"),
        bigquery.SchemaField("trip_hour", "INTEGER"),
        bigquery.SchemaField("source_batch", "INTEGER"),
    ]
    table = bigquery.Table(table_id, schema=schema)
    try:
        table = client.create_table(table)
        print(f"Created table {table.project}.{table.dataset_id}.{table.table_id}")
    except Exception as e:
        print(f"Error creating table: {e}")

def load_to_bigquery(path):
    if os.path.isfile(path):
        if path.lower().endswith(".csv"):
            try:
                client = bigquery.Client()
                table_id = "bike-analytics-project-492312.bike_data.fact_bike_trips"
                
                if not table_exists(client, table_id):
                    print(f"Table {table_id} does not exist")
                    create_table(client, table_id)
                match = re.search(r"trips_clean_(\d{6}).csv", path)
                schema_source = match.group(1)
                query = f"""
                select count(*) as number_rows
                from `bike-analytics-project-492312.bike_data.fact_bike_trips`
                where source_batch = {schema_source}
                """
                query_job = client.query(query)
                results = query_job.result()
                row = next(results)  # get first (and only) row
                
                if row.number_rows == 0:
                    job_config = bigquery.LoadJobConfig(
                        source_format=bigquery.SourceFormat.CSV,
                        skip_leading_rows=1,
                        write_disposition = bigquery.WriteDisposition.WRITE_APPEND,
                    )
                    with open(path, "rb") as source_file:
                        job = client.load_table_from_file(source_file, table_id, job_config=job_config)
                
                    job.result()
                    print(f"{match.group(0)} loaded successfully.")
                else:
                    print(f"Data from {match.group(0)} already exists")

                
                
            except  Exception:
                raise
        else:
            print("File format is wrong it should be a CSV file")
    else:
        print("File does not exist")
    


if __name__ == "__main__":
    if len(sys.argv) > 1:
        path = sys.argv[1]
        try:
            load_to_bigquery(path)
        except Exception as e:
            print(f"Error while loading data: {e}")

    else:
        print("No argument provided")