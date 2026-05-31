import pandas as pd

path = r"C:\Users\saish\Downloads\messy_behavioural_data.csv"

df = pd.read_csv(
    path,
    parse_dates=["account_open_date", "snapshot_month"],
    na_values=["", "NA", "NaN"]
)

# Clean income values like "Rs.42,300"
df["income"] = pd.to_numeric(
    df["income"].astype(str).str.replace(r"[^\d\.]", "", regex=True),
    errors="coerce"
)

print(df.head())
print(df.info())

print (df["income"].describe())