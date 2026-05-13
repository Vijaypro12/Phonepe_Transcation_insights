import pandas as pd
from postgresql import conn, cursor

df = pd.read_csv("data/split_data/aggregated/aggregated_transaction.csv")

for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO aggregated_transcation (year, quarter, category, count, amount)
        VALUES (%s, %s, %s, %s, %s)
    """, (
        int(row['year']),
        int(row['quarter']),
        row['category'],
        int(row['count']),
        float(row['amount'])
    ))

conn.commit()
print("Inserted")