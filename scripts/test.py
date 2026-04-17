from google.cloud import storage
from dotenv import load_dotenv
import os

load_dotenv()

bucket_name = "bike-data-lake"
project_id = os.getenv("GOOGLE_CLOUD_PROJECT")

if not project_id:
    raise ValueError("GOOGLE_CLOUD_PROJECT is not set")
client = storage.Client(project=project_id)
bucket = client.bucket(bucket_name)
folder_path = "raw/"
if not bucket.exists():
    print(f"Bucket {bucket_name} does not exist.")
    bucket = client.create_bucket(bucket_name)
    print(f"Bucket {bucket.name} created.")
    if not folder_path.endswith("/"):
        folder_path += "/"
    blobs = bucket.list_blobs(prefix=folder_path, max_results=1)
    if not any(blobs):
        blob = bucket.blob(folder_path)
        blob.upload_from_string('')

new_blob = bucket.blob("file_to_upload.txt")
new_blob.upload_from_filename("file_to_upload.txt")

blobs = bucket.list_blobs()
for blob in blobs:
    print(blob.name)