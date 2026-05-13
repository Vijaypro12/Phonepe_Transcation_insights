import pandas as pd
from utils import get_all_json_files, load_json, extract_year_quarter

BASE_PATH = "data/map"

data = []

files = get_all_json_files(BASE_PATH)

for file in files:
    content = load_json(file)
    if not content or content["data"] is None:
        continue

    year, quarter = extract_year_quarter(file)

    # MAP TRANSACTION (district)
    if "hoverDataList" in content["data"]:
        for item in content["data"]["hoverDataList"]:
            data.append({
                "year": year,
                "quarter": quarter,
                "district": item["name"],
                "count": item["metric"][0]["count"],
                "amount": item["metric"][0]["amount"]
            })

    # MAP USER
    if "hoverData" in content["data"]:
        for district, values in content["data"]["hoverData"].items():
            data.append({
                "year": year,
                "quarter": quarter,
                "district": district,
                "registeredUsers": values["registeredUsers"],
                "appOpens": values["appOpens"]
            })

df = pd.DataFrame(data)
df.to_csv("data/map_data.csv", index=False)

print("Map ETL Done")