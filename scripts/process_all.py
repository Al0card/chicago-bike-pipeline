from pathlib import Path
from transform import transform
folder = Path("data/raw")
for file in folder.iterdir():
    if file.is_file():
        if (file.name).endswith(".csv"):
            path = "data/raw/"+ file.name
            transform(path)
print("All files processed")
