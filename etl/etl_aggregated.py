import pandas as pd
from utils import get_all_json_files, load_json, extract_year_quarter

BASE_PATH = "data/aggregated"

data = []

files = get_all_json_files(BASE_PATH)

for file in files:
    content = load_json(file)
    if not content or content["data"] is None:
        continue

    year, quarter = extract_year_quarter(file)

    # TRANSACTION
    if "transactionData" in content["data"]:
        for item in content["data"]["transactionData"]:
            for payment in item["paymentInstruments"]:
                data.append({
                    "type": "transaction",
                    "year": year,
                    "quarter": quarter,
                    "category": item["name"],
                    "count": payment["count"],
                    "amount": payment["amount"]
                })

    # USER
    if "usersByDevice" in content["data"] and content["data"]["usersByDevice"] is not None:
        for item in content["data"]["usersByDevice"]:
          data.append({
            "type": "user",
            "brand": item["brand"],
            "count": item["count"],
            "percentage": item["percentage"]
        })

    # INSURANCE
    if "transactionData" in content["data"] and "insurance" in file:
        for item in content["data"]["transactionData"]:
            for payment in item["paymentInstruments"]:
                data.append({
                    "type": "insurance",
                    "year": year,
                    "quarter": quarter,
                    "category": item["name"],
                    "count": payment["count"],
                    "amount": payment["amount"]
                })

df = pd.DataFrame(data)
df.to_csv("data/aggregated_data.csv", index=False)

print("Aggregated ETL Done")