from pathlib import Path
import os.path
from run_pipeline import run_pipeline


folder = Path("data/raw")
files = sorted(folder.glob("*-divvy-tripdata.csv"))
for file in files:
    try:
        print(f"Processing {file.name}")
        run_pipeline(str(file))
    except Exception as e:
        print(f"Processing the file {file.name} failed {e}")

    
print("All files processed")


