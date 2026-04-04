from load.load_to_bigquery import load_to_bigquery
from transform import transform
import sys

if len(sys.argv)>1:
    path = sys.argv[1]
    path_clean_data = transform(path)
    if path_clean_data is not None:
        load_to_bigquery(path_clean_data)
    else:
        print("Transformation failed. Loading step was skipped.")
else:
    print("No argument provided")