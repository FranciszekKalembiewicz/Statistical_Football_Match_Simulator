import pandas as pd
import random
from Matches.PremierLeague2025_26 import matches_PremierLeague, teams_PremierLeague, league_name_PremierLeague


def simulation(league_name, teams_df, match_days):
    df_matches = pd.read_excel(rf"Sezon\{league_name}.xlsx")
    df_matches['HomeSimulationPoints'] = pd.NA
    df_matches['AwaySimulationPoints'] = pd.NA

    for i in range(df_matches.shape[0]):
        values = ["HomeWin", "Draw", "AwayWin"]
        probabilities = [
            df_matches.at[i, "HomeWinProb"],
            df_matches.at[i, "DrawProb"],
            df_matches.at[i, "AwayWinProb"]
        ]
        result = random.choices(values, weights=probabilities, k=1)[0]

        if result == "HomeWin":
            df_matches.at[i, "HomeSimulationPoints"] = 3
            df_matches.at[i, "AwaySimulationPoints"] = 0
        elif result == "AwayWin":
            df_matches.at[i, "HomeSimulationPoints"] = 0
            df_matches.at[i, "AwaySimulationPoints"] = 3
        elif result == "Draw":
            df_matches.at[i, "HomeSimulationPoints"] = 1
            df_matches.at[i, "AwaySimulationPoints"] = 1

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
                        points += df_matches.at[i, 'HomeSimulationPoints']
                if df_matches.at[i, 'Away'] == club:
                    if df_matches.at[i, 'MatchWeek'] in match_days:
                        points += df_matches.at[i, 'AwayPoints']
                    else:
                        points += df_matches.at[i, 'AwaySimulationPoints']

            prediction_data[club].append(points)
    df = pd.DataFrame((prediction_data.items()), columns=['Team', 'SimulatedPoints'])
    df["SimulatedPoints"] = df["SimulatedPoints"].str[0]
    df = df.sort_values(by="SimulatedPoints", ascending=False).reset_index(drop=True)

    return df

def monte_carlo_simulation(league_name, teams_df, match_days):
    num_simulations = 10
    teams_places = {}
    clubs = teams_df["Club"].tolist()
    for club in clubs:
        teams_places[club] = []

    for _ in range(num_simulations):
        df = simulation(league_name, teams_df, match_days)
        for index, row in df.iterrows():
            teams_places[row["Team"]].append(index + 1)

    return teams_places

# print(simulation(league_name_PremierLeague, teams_PremierLeague, [1,2,3,4,5]))
monte_carlo_simulation(league_name_PremierLeague, teams_PremierLeague, [1,2,3,4,5])