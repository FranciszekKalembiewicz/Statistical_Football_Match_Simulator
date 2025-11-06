import json
import csv
import requests
import pandas as pd

API_URL = "https://dataviz.theanalyst.com/opta-power-rankings/pr-reference.json"

with open(r"Data\data.json", "w", encoding="utf-8") as f:
    response = requests.get(API_URL)
    data = response.json()
    json.dump(data, f, ensure_ascii=False, indent=2)


with open(r"Data\data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Prepare CSV
with open(r"Data\ranking.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["contestantName", "rank", "currentRating"])

    for item in data:
        writer.writerow([item.get("contestantName"), item.get("rank"), item.get("currentRating")])

# Convert CSV to Excel with pandas
df = pd.read_csv(r"Data\ranking.csv")

df.columns = ["Team", "Rank", "Rating"]

df.to_excel(r"Data\data.xlsx", index=False)