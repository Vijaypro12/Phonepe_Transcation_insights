import pandas as pd
from utils import get_all_json_files, load_json, extract_year_quarter

BASE_PATH = "data/top"

data = []

files = get_all_json_files(BASE_PATH)

for file in files:
    content = load_json(file)

    if not content or content.get("data") is None:
        continue

    year, quarter = extract_year_quarter(file)
    data_block = content["data"]

    # 🔹 STATES
    if data_block.get("states"):
        for item in data_block["states"]:
            name = item.get("name") or item.get("entityName")

            metric = item.get("metric", {})
            if isinstance(metric, list):
                metric = metric[0] if metric else {}

            data.append({
                "type": "state",
                "year": year,
                "quarter": quarter,
                "name": name,
                "count": metric.get("count"),
                "amount": metric.get("amount")
            })

    # 🔹 DISTRICTS
    if data_block.get("districts"):
        for item in data_block["districts"]:
            name = item.get("name") or item.get("entityName")

            metric = item.get("metric", {})
            if isinstance(metric, list):
                metric = metric[0] if metric else {}

            data.append({
                "type": "district",
                "year": year,
                "quarter": quarter,
                "name": name,
                "count": metric.get("count"),
                "amount": metric.get("amount")
            })

    # 🔹 PINCODES
    if data_block.get("pincodes"):
        for item in data_block["pincodes"]:
            name = item.get("name") or item.get("entityName")

            metric = item.get("metric", {})
            if isinstance(metric, list):
                metric = metric[0] if metric else {}

            data.append({
                "type": "pincode",
                "year": year,
                "quarter": quarter,
                "name": name,
                "count": metric.get("count"),
                "amount": metric.get("amount")
            })

df = pd.DataFrame(data)
df.to_csv("data/top_data.csv", index=False)

print("Top ETL Done")
