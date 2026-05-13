import pandas as pd
from postgresql import conn, cursor

df = pd.read_csv("data/split_data/map/map_transaction.csv")

# Keep only needed columns
df = df[["year", "quarter", "district", "count", "amount"]]

df = df.dropna()

for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO map_data (year, quarter, district, count, amount)
        VALUES (%s, %s, %s, %s, %s)
    """, (
        int(row['year']),
        int(row['quarter']),
        row['district'],
        int(row['count']),
        float(row['amount'])
    ))

conn.commit()
print("map_data inserted")