import pandas as pd
import json
from data_ingestion.openf1_client import get_season_results
result = get_season_results(2024)
print(result)