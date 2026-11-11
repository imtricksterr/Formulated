import pandas as pd

dataset = pd.read_csv("data/raw/season_2024_2025.csv")

drivers_df = dataset[["name_acronym", "full_name"]].drop_duplicates()

print(drivers_df.shape)
print(drivers_df.head())

