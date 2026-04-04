import pandas as pd
# Tell pandas to show all columns
pd.set_option('display.max_columns', None)
df = pd.read_csv("data/processed/trips_clean_202501.csv")
df.info()
print("columns:", df.columns)

print("shape :", df.shape)
print("numer of nulls in station related columns:")
station_cols = ['start_station_name', 'start_station_id', 'end_station_name','end_station_id']
for col in station_cols:
    print(col  ,df[col].isnull().sum())

print("numer of nulls in  generated columns:")
generated_cols = ['duration_seconds', 'trip_date', 'trip_year', 'trip_month', 'trip_weekday', 'trip_hour']
for col in generated_cols:
    print(col, df[col].isnull().sum())

print(df.head())