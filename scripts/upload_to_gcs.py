from pathlib import Path
from google.cloud import storage
from dotenv import load_dotenv
import os

load_dotenv()

folder = Path("data/raw")

files = sorted(folder.glob("*-divvy-tripdata.csv"))

for file in files:
    if file.is_file() and (file.name).lower().endswith(".csv"):
        print(file.name)
    