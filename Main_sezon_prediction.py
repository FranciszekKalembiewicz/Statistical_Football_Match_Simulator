import json
import csv
import requests
import pandas as pd
import numpy as np
from pathlib import Path

from Data_upload_api import data_upload_api
from Statistic_prediction import match_score_propability
from League_generator import generate_matches_df
from League_update import add_match_result, update_league
from Table_prediction import table_prediction, table_xlsx

from Matches.PremierLeague2025_26 import matches_PremierLeague, teams_PremierLeague, league_name_PremierLeague
from Matches.LaLiga2025_26 import matches_LaLiga, teams_LaLiga, league_name_LaLiga

def sezon_full_prediction(teams, league_name, matches):
    #Data_upload_api.py
    data_upload_api()
    df_rating = pd.read_excel(r"Data\data.xlsx")

    #League_generator.py
    path = Path(rf"Sezon\{league_name}.xlsx")
    if not path.exists():
        fixtures = generate_matches_df(teams, df_rating)
        fixtures.to_excel(path, index=False)

    #League_update.py
    df_league = pd.read_excel(rf"Sezon\{league_name}.xlsx")
    for match in matches:
        add_match_result(df_league, match["match_week"], match["home"], match["home_goals"], match["away"], match["away_goals"], )
    df_league = update_league(teams, df_league)
    df_league.to_excel(rf"Sezon\{league_name}.xlsx", index=False)

    #Table_prediction.py
    #Create Prediction folder for sezon
    path = Path(rf"Prediction\{league_name}")
    if not path.exists():
        path.mkdir(parents=True)

    matchday = sorted({0} | {m["match_week"] for m in matches})
    for i in range(1, len(matchday) + 1):
        path = Path(rf"Prediction\{league_name}\Predicted_{league_name}_table_matchday_{max(matchday[:i])}.xlsx")
        if not path.exists():
            df_table = table_xlsx(rf"Sezon\{league_name}.xlsx", teams, matchday[:i])
            df_table.to_excel(
                rf"Prediction\{league_name}\Predicted_{league_name}_table_matchday_{max(matchday[:i])}.xlsx",
                index=False)

#PremierLeague:
sezon_full_prediction(teams_PremierLeague, league_name_PremierLeague, matches_PremierLeague)

# #LaLiga:
sezon_full_prediction(teams_LaLiga, league_name_LaLiga, matches_LaLiga)