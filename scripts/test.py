import sys
import re
from pathlib import Path
import os.path


path = sys.argv[1]


filename = Path(path).name
match = re.search(r"^(\d{4}(0[1-9]|1[0-2]))-divvy-tripdata.csv$", filename)
if match:
    print(match)
    print(match.group())

else:
    print("unexpected file name it should follow the convetion YYYYMMYYYYMM-divvy-tripdata.csv")
