from google.cloud import storage
from dotenv import load_dotenv
import os
import sys
from pathlib import Path


def upload_to_gcs(bucket_name, project_id, file):
    if not project_id:
        raise ValueError("GOOGLE_CLOUD_PROJECT is not set")
    client = storage.Client(project=project_id)
    bucket = client.bucket(bucket_name)
    
    if not bucket.exists():
        print(f"Bucket {bucket_name} does not exist.")
        bucket = client.create_bucket(bucket_name)
        print(f"Bucket {bucket.name} created.")
        
    blob = bucket.blob(str(file))
    if blob.exists():
        print(f"File {file.name} already exists, skipping")
    else:
        local_path = str(file)
        gcs_path = f"raw/{file.name}"
        new_blob = bucket.blob(gcs_path)
        new_blob.upload_from_filename(local_path, timeout=1200)
        print(f"File {file.name} was uploaded.")
        # prefix = "raw/"
        # blobs = bucket.list_blobs(prefix=prefix)
        # for blob in blobs:
        #     print(blob.name)

if len(sys.argv) > 1:
    # load_dotenv()

    # bucket_name = "bike-data-lake"
    # project_id = os.getenv("GOOGLE_CLOUD_PROJECT")
    file = Path(sys.argv[1])
    if file.is_file():
        if (file.name).lower().endswith(".csv"):
            load_dotenv()
            bucket_name = "bike-data-lake"
            project_id = os.getenv("GOOGLE_CLOUD_PROJECT")
            upload_to_gcs(bucket_name, project_id, file )
        else:
            print("The file is not in the csv format")
    else:
        print("File does not exist")
else:
    print("No file was passed")


