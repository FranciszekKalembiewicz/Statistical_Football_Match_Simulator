# table_and_simulation_combined.py
import pandas as pd
import numpy as np
from tqdm import tqdm


def run_table_predictions(league_filename, teams_df, match_days, table_places, number_simulations, random_seed=None):
    if random_seed is not None:
        rng = np.random.default_rng(random_seed)
    else:
        rng = np.random.default_rng()

    df_matches = pd.read_excel(league_filename)
    clubs = teams_df['Club'].tolist()
    T = len(clubs)
    club_to_idx = {club: idx for idx, club in enumerate(clubs)}
    idx_to_club = {idx: club for club, idx in club_to_idx.items()}

    base_points = np.zeros(T, dtype=np.int32)
    simulate_mask = ~df_matches['MatchWeek'].isin(match_days).to_numpy()

    for i in range(df_matches.shape[0]):
        home = df_matches.at[i, 'Home']
        away = df_matches.at[i, 'Away']
        mw = df_matches.at[i, 'MatchWeek']

        if mw in match_days:
            hp = int(df_matches.at[i, 'HomePoints']) if pd.notna(df_matches.at[i, 'HomePoints']) else 0
            ap = int(df_matches.at[i, 'AwayPoints']) if pd.notna(df_matches.at[i, 'AwayPoints']) else 0
        else:
            hp = int(df_matches.at[i, 'HomeExp']) if pd.notna(df_matches.at[i, 'HomeExp']) else 0
            ap = int(df_matches.at[i, 'AwayExp']) if pd.notna(df_matches.at[i, 'AwayExp']) else 0

        if home in club_to_idx:
            base_points[club_to_idx[home]] += hp
        else:
            pass

        if away in club_to_idx:
            base_points[club_to_idx[away]] += ap
        else:
            pass

    M = df_matches.shape[0]
    home_idx = np.array([club_to_idx.get(h, -1) for h in df_matches['Home']], dtype=np.int32)
    away_idx = np.array([club_to_idx.get(a, -1) for a in df_matches['Away']], dtype=np.int32)

    home_win_prob = df_matches['HomeWinProb'].to_numpy(dtype=float)
    draw_prob = df_matches['DrawProb'].to_numpy(dtype=float)
    away_win_prob = df_matches['AwayWinProb'].to_numpy(dtype=float)

    probs = np.vstack([home_win_prob, draw_prob, away_win_prob]).T

    matches_to_simulate = np.where(simulate_mask)[0].tolist()

    teams_places = {club: [] for club in clubs}

    for _ in tqdm(range(number_simulations), desc="Monte-Carlo"):
        sim_points = base_points.copy()

        for m in matches_to_simulate:
            h_idx = home_idx[m]
            a_idx = away_idx[m]
            if h_idx == -1 or a_idx == -1:
                continue

            p = probs[m]
            if np.isnan(p).any():
                p = np.array([1 / 3, 1 / 3, 1 / 3], dtype=float)
            r = rng.choice(3, p=p)
            if r == 0:
                sim_points[h_idx] += 3
            elif r == 1:
                sim_points[h_idx] += 1
                sim_points[a_idx] += 1
            else:
                sim_points[a_idx] += 3

        order = np.argsort(-sim_points)
        for place_idx, team_idx in enumerate(order):
            team_name = idx_to_club[int(team_idx)]
            teams_places[team_name].append(place_idx + 1)

    proc_table = {}
    total = number_simulations
    for team, places in teams_places.items():
        arr = np.array(places, dtype=np.int32)
        team_result = {}
        for category, accepted_places in table_places.items():
            mask = np.isin(arr, accepted_places)
            team_result[category] = mask.sum() / total
        proc_table[team] = team_result

    def to_percent(x):
        return f"{x * 100:.2f}%"

    table_rows = []
    for club in clubs:
        row = {}
        row["Rank"] = pd.NA
        row["Team"] = club
        row["WIN"] = to_percent(proc_table[club].get("win", 0.0))
        if table_places.get("champions_league"):
            row[f"TOP{max(table_places['champions_league'])}"] = to_percent(
                proc_table[club].get('champions_league', 0.0))
        if table_places.get("europa_league"):
            row[f"TOP{max(table_places['europa_league'])}"] = to_percent(proc_table[club].get('europa_league', 0.0))
        if table_places.get("conference_league"):
            row[f"TOP{max(table_places['conference_league'])}"] = to_percent(
                proc_table[club].get('conference_league', 0.0))
        row["RELEGATION"] = to_percent(proc_table[club].get("relegation", 0.0))
        row["ExpPoints"] = int(base_points[club_to_idx[club]])
        table_rows.append(row)

    table_rows = sorted(table_rows, key=lambda x: x["ExpPoints"], reverse=True)
    for i, r in enumerate(table_rows):
        r["Rank"] = i + 1

    df_table = pd.DataFrame(table_rows)
    return df_table