import pandas as pd
import sys
import re
import os.path
from pathlib import Path


def transform(path):
    
    if os.path.isfile(path):
        if path.lower().endswith(".csv"):
            filename = Path(path).name
            match = re.search(r"^(\d{4}(0[1-9]|1[0-2]))-divvy-tripdata\.csv$", filename)
            if match:
                df = pd.read_csv(path, parse_dates= ['started_at', 'ended_at']) 

                colums_to_remove = ['start_lat', 'start_lng', 'end_lat', 'end_lng']
                df = df.drop(columns = colums_to_remove)

                df["duration_seconds"] = (df['ended_at'] - df['started_at']).dt.total_seconds()

                df["trip_date"] = df["started_at"].dt.normalize()
                df["trip_year"] = df["started_at"].dt.year
                df["trip_month"] = df["started_at"].dt.month
                df["trip_weekday"] = df["started_at"].dt.day_name()
                df["trip_hour"] = df["started_at"].dt.hour
                df["source_batch"] = match.group(1)
                save_path = "data/processed"
                if not os.path.isdir(save_path):
                    os.makedirs(save_path)
                output_path = f'data/processed/trips_clean_{match.group(1)}.csv'
                df.to_csv(output_path, index=False)
                print(f"file: trips_clean_{match.group(1)}.csv saved")
                return output_path
            else:
                print("unexpected file name it should follow the convetion YYYYMM-divvy-tripdata.csv")
                return None
        else:
                print("should be a csv file")
                return None
    else:
        print("Enter an existing file")
        return None
    
    


if __name__ == "__main__":

    if len(sys.argv) > 1:
        path = sys.argv[1]
     
        transform(path)
    else:
        print("no argument passed")
