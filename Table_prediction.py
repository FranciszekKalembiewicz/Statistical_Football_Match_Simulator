import pandas as pd
from Matches.PremierLeague2025_26 import league_name_PremierLeague, teams_PremierLeague, matchday_PremierLeague

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

def table_xlsx(league_name, teams_df, MatchDay):
    clubs = teams_df["Club"].tolist()
    table = []
    points = table_prediction(league_name, teams_df, MatchDay)

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

#Table for prem:
df_table = table_xlsx(league_name_PremierLeague, teams_PremierLeague, matchday_PremierLeague)
short_name = league_name_PremierLeague = league_name_PremierLeague.split("\\")[-1]
df_table.to_excel(rf"Prediction\Predicted_{short_name}_table_matchday_{max(matchday_PremierLeague)}.xlsx", index=False)