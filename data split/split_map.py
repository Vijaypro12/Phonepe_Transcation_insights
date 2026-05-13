import pandas as pd

df = pd.read_csv("data/map_data.csv")

df = df[["year", "quarter", "district", "count", "amount"]]

df.to_csv("data/split_data/map/map_transaction.csv", index=False)

print("Cleaned map file")