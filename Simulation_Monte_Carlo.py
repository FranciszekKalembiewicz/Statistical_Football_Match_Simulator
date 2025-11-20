import pandas as pd
import random
from tqdm import tqdm
from Matches.PremierLeague2025_26 import matches_PremierLeague, teams_PremierLeague, league_name_PremierLeague, table_places_PremierLeague


def simulation(league_name, teams_df, match_days):
    df_matches = pd.read_excel(rf"{league_name}")
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

def monte_carlo_simulation(league_name, teams_df, match_days, number_simulations):
    num_simulations = number_simulations
    teams_places = {}
    clubs = teams_df["Club"].tolist()
    for club in clubs:
        teams_places[club] = []

    for _ in tqdm(range(num_simulations)):
        df = simulation(league_name, teams_df, match_days)
        for index, row in df.iterrows():
            teams_places[row["Team"]].append(index + 1)
    return teams_places

def table_update_monte_carlo(league_name, teams_df, match_days, table_places, number_simulations):
    teams_places = monte_carlo_simulation(league_name, teams_df, match_days, number_simulations)
    proc_table = {}
    for team, places in teams_places.items():
        total = len(places)
        team_result = {}

        for category, accepted_places in table_places.items():
            count = sum(place in accepted_places for place in places)
            percentage = count / total
            team_result[category] = percentage

        proc_table[team] = team_result

    return proc_table

# print(simulation(league_name_PremierLeague, teams_PremierLeague, [1,2,3,4,5]))
# print(table_update_monte_carlo(league_name_PremierLeague, teams_PremierLeague, [1,2,3,4,5], table_places_PremierLeague))