import pandas as pd
import random

def simulation(league_name, teams_df, match_days):
    df_matches = pd.read_excel(rf"Sezon\{league_name}.xlsx")
    df_matches.insert("HomeSimulationPoints", pd.NA)
    df_matches.insert("AwaySimulationPoints", pd.NA)

    values = ["HomeWin", "Draw", "AwayWin"]
    probabilities = [0.42, 0.26, 0.32]
    result = random.choices(values, weights=probabilities, k=1)[0]


    clubs = teams_df["Club"].tolist()
    prediction_data = {}
    for club in clubs:
        prediction_data[club] = []
        points = 0
        for i in range(0, df_matches.shape[0]):
            if df_matches.at[i, 'Home'] == club:
                if df_matches.at[i, 'MatchWeek'] in match_days:
                    points += df_matches.at[i, 'HomePoints']
                else:
                    points += df_matches.at[i, 'HomeExp']
            if df_matches.at[i, 'Away'] == club:
                if df_matches.at[i, 'MatchWeek'] in match_days:
                    points += df_matches.at[i, 'AwayPoints']
                else:
                    points += df_matches.at[i, 'AwayExp']
        prediction_data[club].append(points)

    return prediction_data

# def table_xlsx(league_name, teams_df, matchday):
#     clubs = teams_df["Club"].tolist()
#     table = []
#     points = table_prediction(league_name, teams_df, matchday)
#
#     for i in range(len(clubs)):
#             table.append({
#                 "Rank": pd.NA,
#                 "Team": clubs[i],
#                 "ExpPoints": points[clubs[i]],
#             })
#     table = sorted(table, key=lambda x: x["ExpPoints"], reverse=True)
#     for i in range(len(table)):
#         table[i]["Rank"] = i + 1
#
#     df_table = pd.DataFrame(table)
#     return df_table