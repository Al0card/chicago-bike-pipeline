from pathlib import Path
from google.cloud import storage
from dotenv import load_dotenv
import os

load_dotenv()


    if file.is_file() and (file.name).lower().endswith(".csv"):
        print(file.name)
    