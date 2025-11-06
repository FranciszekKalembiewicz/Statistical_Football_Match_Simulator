import pandas as pd
from Matches.PremierLeague2025_26 import league_name_PremierLeague, teams_PremierLeague

def table_prediction(file_name, teams_df, match_days):
    df_maches = pd.read_excel(file_name)
    clubs = teams_df["Club"].tolist()
    table_data = {}
    for club in clubs:
        points = 0
        for i in range(0, df_maches.shape[0]):
            if df_maches.at[i, 'Home'] == club:
                if df_maches.at[i, 'MatchWeek'] in match_days:
                    points += df_maches.at[i, 'HomePoints']
                else:
                    points += df_maches.at[i, 'HomeExp']
            if df_maches.at[i, 'Away'] == club:
                if df_maches.at[i, 'MatchWeek'] in match_days:
                    points += df_maches.at[i, 'AwayPoints']
                else:
                    points += df_maches.at[i, 'AwayExp']
        table_data[club] = points
    return table_data

MatchDay = [1, 2, 3, 4, 5, 6, 7, 8]
table = table_prediction(league_name_PremierLeague, teams_PremierLeague, MatchDay)

print(table["Arsenal"])
print(table)

def table_xlsx(league_name, teams_df, MatchDay):
    clubs = teams_df["Club"].tolist()
    table = []
    points = table_prediction(league_name, teams_df, MatchDay)

    for i in range(len(clubs)):
            table.append({
                "Team": clubs[i],
                "ExpPoints": points[clubs[i]],
            })

    df_table = pd.DataFrame(table)
    return df_table

#Table for prem:
df_table = table_xlsx(league_name_PremierLeague, teams_PremierLeague, MatchDay)

df_table.to_excel("Predicted table in", index=False)