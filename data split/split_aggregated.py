import pandas as pd

df = pd.read_csv("data/aggregated_data.csv")


df_transaction = df[df["type"] == "transaction"]
df_user = df[df["type"] == "user"]
df_insurance = df[df["type"] == "insurance"]


df_transaction.to_csv("data/split_data/aggregated/aggregated_transaction.csv", index=False)
df_user.to_csv("data/split_data/aggregated/aggregated_user.csv", index=False)
df_insurance.to_csv("data/split_data/aggregated/aggregated_insurance.csv", index=False)

print("Split completed")