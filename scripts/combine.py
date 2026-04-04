import pandas as pd
from pathlib import Path
folder = Path("data/processed")
metadata = {}
files = sorted(folder.glob("trips_clean_*.csv"))
if files:
    all_data = []
    row_counts = 0
    for i in range(len(files)):
        df = pd.read_csv(files[i])
        all_data.append(df)
        metadata[i] = df.columns
        row_counts += df.shape[0]
    temp = metadata[0]
   
    for i in range(1, len(metadata)):
        if not metadata[i].equals(temp):
            raise ValueError(f"Schema mismatch in files:\n"
                             f"- {files[0].name}\n"
                             f"- {files[i].name}")
        

    
    result = pd.concat(all_data, axis=0, ignore_index=True)
    result.to_csv('data/processed/trips_all.csv', index=False)
    if result.shape[0] == row_counts:
        print(f"results row counts: {result.shape[0]}, row counts of different datasets: {row_counts}")
        print("Row counts is valid")
    else:
        print("Mismatch in row count there is a problem")
    if result["ride_id"].duplicated().any():
        print(f"number of duplciates {result['ride_id'].duplicated().sum()}")
    else:
        print("No duplicates")
else:
   raise ValueError("No files found that match trips_clean_*.csv")