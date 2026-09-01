import pandas as pd
import requests
import json

def fetch_season(year): 

    sessions_data = requests.get(
        f"https://api.openf1.org/v1/sessions?year={year}"
    ).json()


    sessions_df = pd.DataFrame(sessions_data)
    race_sessions_df = sessions_df[sessions_df["session_name"] == "Race"]

    return race_sessions_df
