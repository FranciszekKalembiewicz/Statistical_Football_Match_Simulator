import pandas as pd
from Matches.PremierLeague2025_26 import league_name_PremierLeague, teams_PremierLeague, matches_PremierLeague

def table_prediction(file_name, teams_df, match_days):
    df_matches = pd.read_excel(file_name)
    clubs = teams_df["Club"].tolist()
    table_data = {}
    for club in clubs:
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
        table_data[club] = points
    return table_data

def table_xlsx(league_name, teams_df, matchday):
    clubs = teams_df["Club"].tolist()
    table = []
    points = table_prediction(league_name, teams_df, matchday)

    for i in range(len(clubs)):
            table.append({
                "Rank": pd.NA,
                "Team": clubs[i],
                "ExpPoints": points[clubs[i]],
            })
    table = sorted(table, key=lambda x: x["ExpPoints"], reverse=True)
    for i in range(len(table)):
        table[i]["Rank"] = i + 1

    df_table = pd.DataFrame(table)
    return df_table

# #Table for prem:
#    path = Path(rf"Prediction\{league_name_PremierLeague}")
#   if not path.exists():
#        path.mkdir(parents=True)
# matchday_PremierLeague = sorted({0} | {m["match_week"] for m in matches_PremierLeague})
# for i in range(1, len(matchday_PremierLeague) + 1):
#     df_table = table_xlsx(rf"Sezon\{league_name_PremierLeague}.xlsx", teams_PremierLeague, matchday_PremierLeague[:i])
#     df_table.to_excel(rf"Prediction\PremierLeague2025_26\Predicted_{league_name_PremierLeague}_table_matchday_{max(matchday_PremierLeague[:i])}.xlsx", index=False)