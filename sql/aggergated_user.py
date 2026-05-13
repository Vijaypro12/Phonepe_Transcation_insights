import pandas as pd
from postgresql import conn, cursor

df = pd.read_csv("data/split_data/aggregated/aggregated_user.csv")

for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO aggregated_user (count, brand,percentage)
        VALUES (%s, %s, %s)
    """, (
        int(row['count']),
        row['brand'],
        float(row['percentage'])
    ))


conn.commit()
print("Inserted")   