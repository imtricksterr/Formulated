from data_ingestion.openf1_client import fetch_and_merge

result = fetch_and_merge(9480)
print(result.shape)
print(result[["driver_number", "full_name", "position", "points"]])