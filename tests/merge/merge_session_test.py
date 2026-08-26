import pandas as pd
import json

with open("race_results_test.json", encoding="utf-16") as f: 
    results_data = json.load(f)

with open("drivers_test.json", encoding="utf-16") as f: 
    drivers_data = json.load(f)

results_df = pd.DataFrame(results_data)
drivers_df = pd.DataFrame(drivers_data)

merged_df = pd.merge(results_df, drivers_df, on="driver_number")
print(merged_df.shape)
print(merged_df[["driver_number", "full_name", "position", "points"]])
