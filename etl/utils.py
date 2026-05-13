import os
import json

def get_all_json_files(base_path):
    json_files = []
    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file.endswith(".json"):
                json_files.append(os.path.join(root, file))
    return json_files


def load_json(file_path):
    try:
        with open(file_path, "r") as f:
            return json.load(f)
    except:
        return None


def extract_year_quarter(file_path):
    parts = file_path.replace("\\", "/").split("/")
    
    # year and quarter extraction
    year = None
    quarter = None

    for part in parts:
        if part.isdigit() and len(part) == 4:
            year = int(part)
        if part.endswith(".json"):
            quarter = int(part.replace(".json", ""))

    return year, quarter



    