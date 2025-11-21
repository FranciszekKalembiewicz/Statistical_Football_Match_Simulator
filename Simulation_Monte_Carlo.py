import pandas as pd
import random
from tqdm import tqdm
from Matches.PremierLeague2025_26 import matches_PremierLeague, teams_PremierLeague, league_name_PremierLeague, table_places_PremierLeague


def simulation(league_name, teams_df, match_days):
    df_matches = pd.read_excel(rf"{league_name}")
    clubs = teams_df["Club"].tolist()
    prediction_points = {club: 0 for club in clubs}

    for i in range(df_matches.shape[0]):
        home = df_matches.at[i, 'Home']
        away = df_matches.at[i, 'Away']
        week = df_matches.at[i, 'MatchWeek']

        if week in match_days:
            home_points = int(df_matches.at[i, 'HomePoints'])
            away_points = int(df_matches.at[i, 'AwayPoints'])

        else:
            probs = [
                df_matches.at[i, "HomeWinProb"],
                df_matches.at[i, "DrawProb"],
                df_matches.at[i, "AwayWinProb"]
            ]

            result = random.choices(["HomeWin", "Draw", "AwayWin"], weights=probs, k=1)[0]

            if result == "HomeWin":
                home_points = 3
                away_points = 0
            elif result == "AwayWin":
                home_points = 0
                away_points = 3
            elif result == "Draw":
                home_points = 1
                away_points = 1
            else:
                print("Error in simulation")

        prediction_points[home] += home_points
        prediction_points[away] += away_points

    df = pd.DataFrame(list(prediction_points.items()), columns=['Team', 'SimulatedPoints'])
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