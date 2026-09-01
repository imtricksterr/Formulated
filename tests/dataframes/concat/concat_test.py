import pandas as pd
import requests
import json
import time

def fetch_and_merge(session_key):

    results_data = requests.get(
        "https://api.openf1.org/v1/session_result",
        params={"session_key": session_key}
    ).json()

    drivers_data = requests.get(
        "https://api.openf1.org/v1/drivers",
        params={"session_key": session_key}
    ).json()

    try: 
        results_df = pd.DataFrame(results_data)
        drivers_df = pd.DataFrame(drivers_data)
    except ValueError:
        print(f"Problem with session_key {session_key}: {results_data}")
        return None

    return pd.merge(results_df, drivers_df, on="driver_number")


def get_race_session_keys(year):
    session_data = requests.get(
        f"https://api.openf1.org/v1/sessions?year={year}",
    ).json()

    sessions_df = pd.DataFrame(session_data)
    
    race_sessions_df = sessions_df[sessions_df["session_name"] == "Race"]

    race_session_keys = race_sessions_df["session_key"].tolist()

    return race_session_keys


def concat():

    keys_2024 = get_race_session_keys(2024)    
    keys_2025 = get_race_session_keys(2025)

    dataset = pd.DataFrame()

    for key in keys_2024:
        result = fetch_and_merge(key)
        if result is not None:
            dataset = pd.concat([dataset, result], ignore_index=True)
        time.sleep(2)


    for key in keys_2025:
        result = fetch_and_merge(key)
        if result is not None:
            dataset = pd.concat([dataset, result], ignore_index=True)
        time.sleep(2)

    return dataset

dataset = concat()

# TEST THESE LATER
print(dataset["session_key".nunique()])
print(dataset["position"] == 1)
