from google.cloud import bigquery
from google.cloud.exceptions import NotFound
import re
from pathlib import Path
import sys



client = bigquery.Client()
table_id = "bike-analytics-project-492312.bike_data.fact_bike_trips"


schema_source = 202505

query = f"""
select count(*) as number_rows
from `bike-analytics-project-492312.bike_data.fact_bike_trips`
where source_batch = {schema_source}
"""





query_job = client.query(query)

results = query_job.result()


row = next(results)  # get first (and only) row
print(row.number_rows)
    