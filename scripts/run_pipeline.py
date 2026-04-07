from load.load_to_bigquery import load_to_bigquery
from transform import transform
import sys

def run_pipeline(path):
    try:
        path_clean_data = transform(path)
        if path_clean_data is not None:
            load_to_bigquery(path_clean_data)
        else:
            print("Transformation failed. Loading step was skipped.")
    except Exception as e:
        print(f"Erron while runing pipline: {e}")
        

if __name__ == "__main__":
    
    if len(sys.argv)>1:
        path = sys.argv[1]
        run_pipeline(path)
    else:
        print("No argument provided")
    