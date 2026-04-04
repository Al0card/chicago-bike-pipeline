import sys
from google.cloud import bigquery
import os.path

def load_to_bigquery(path):
    if os.path.isfile(path):
        if path.lower().endswith(".csv"):
            try:
                client = bigquery.Client()
                table_id = "bike-analytics-project-492312.bike_data.fact_bike_trips"
                job_config = bigquery.LoadJobConfig(
                    source_format=bigquery.SourceFormat.CSV,
                    skip_leading_rows=1,
                    write_disposition = bigquery.WriteDisposition.WRITE_APPEND,
                )
                with open(path, "rb") as source_file:
                    job = client.load_table_from_file(source_file, table_id, job_config=job_config)
            
                job.result()
                print("Data loaded successfully.")
            except  Exception as e:
                print(f"Error while loading data: {e}")
                sys.exit(1)
        else:
            print("File format is wrong it should be a CSV file")
    else:
        print("File does not exist")
    


def main():
    if len(sys.argv) > 1:
        path = sys.argv[1]
        load_to_bigquery(path)
    else:
        print("No argument provided")