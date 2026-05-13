import pandas as pd
from postgresql import conn, cursor

df = pd.read_csv("data/split_data/top/top_data.csv")

# Clean data
df = df.dropna()
df["type"] = df["type"].str.lower().str.strip()

for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO top_data (type, year, quarter, name, count, amount)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (
        row['type'],
        int(row['year']),
        int(row['quarter']),
        row['name'],
        int(row['count']),
        float(row['amount'])
    ))

conn.commit()
print("top_data inserted")