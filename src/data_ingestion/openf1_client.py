import pandas as pd
import requests
import json

def fetch_and_merge(session_key):

    results_data = requests.get(
        "https://api.openf1.org/v1/session_result",
        params={"session_key": session_key}
    ).json()


    drivers_data = requests.get(
        "https://api.openf1.org/v1/drivers",
        params={"session_key": session_key}
    ).json()

    results_df = pd.DataFrame(results_data)
    drivers_df = pd.DataFrame(drivers_data)

    return pd.merge(results_df, drivers_df, on="driver_number")





def get_season_results(year): pass