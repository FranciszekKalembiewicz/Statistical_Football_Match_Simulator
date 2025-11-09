import json
import csv
import requests
import pandas as pd
import numpy as np
from pathlib import Path

from Data_upload_api import data_upload_api
from League_generator import generate_matches_df
from Statistic_prediction import match_score_propability
from Matches.PremierLeague2025_26 import matches_PremierLeague, teams_PremierLeague, league_name_PremierLeague


def sezon_full_prediction(teams, league_name):
    #Data_upload_api.py
    data_upload_api()
    df_rating = pd.read_excel(r"Data\data.xlsx")

    #League_generator.py
    path = Path(rf"Sezon\{league_name}.xlsx")
    if not path.exists():
        fixtures = generate_matches_df(teams, df_rating)
        fixtures.to_excel(path, index=False)

    #League_update.py



#PremierLeague:
sezon_full_prediction(teams_PremierLeague,league_name_PremierLeague)