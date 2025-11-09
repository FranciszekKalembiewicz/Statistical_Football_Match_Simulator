import pandas as pd
from Statistic_prediction import match_score_propability
from Matches.PremierLeague2025_26 import matches_PremierLeague, teams_PremierLeague, league_name_PremierLeague

def add_match_result(df_league, match_week, home_team, home_goals, away_team, away_goals,):
    mask = df_league['Home'].eq(home_team) & df_league['Away'].eq(away_team)
    df_league.loc[mask, 'HomeGoals'] = home_goals
    df_league.loc[mask, 'AwayGoals'] = away_goals
    df_league.loc[mask, 'MatchWeek'] = match_week

def update_league(teams_df, df_league):
    clubs = teams_df["Club"].tolist()

    for i in range(len(clubs)):
        for j in range(i + 1, len(clubs)):

            # Spring round
            win1, draw, win2, exp1, exp2 = match_score_propability(
                df_rating.loc[df_rating["Team"] == clubs[i], "Rating"].values[0],
                df_rating.loc[df_rating["Team"] == clubs[j], "Rating"].values[0],
                home_club_1=True,
                home_club_2=False
            )

            mask = df_league['Home'].eq(clubs[i]) & df_league['Away'].eq(clubs[j])
            if not pd.isna(df_league.loc[mask, "HomeGoals"].values[0]):
                if df_league.loc[mask, "HomeGoals"].values[0] > df_league.loc[mask, "AwayGoals"].values[0]:
                    df_league.loc[mask, 'Result'] = str(clubs[i]) # Home win
                elif df_league.loc[mask, "HomeGoals"].values[0] < df_league.loc[mask, "AwayGoals"].values[0]:
                    df_league.loc[mask, 'Result'] = str(clubs[j]) # Away win
                elif df_league.loc[mask, "HomeGoals"].values[0] == df_league.loc[mask, "AwayGoals"].values[0]:
                    df_league.loc[mask, 'Result'] = "Draw"  # Draw
                else:
                    df_league.loc[mask, 'Result'] = pd.NA,

            if pd.isna(df_league.loc[mask, "HomeGoals"].values[0]):
                df_league.loc[mask, 'HomeRating'] = df_rating.loc[df_rating["Team"] == clubs[i], "Rating"].values[0],
                df_league.loc[mask, 'AwayRating'] = df_rating.loc[df_rating["Team"] == clubs[j], "Rating"].values[0],
                df_league.loc[mask, 'HomeWinProb'] = win1
                df_league.loc[mask, 'AwayWinProb'] = win2
                df_league.loc[mask, 'DrawProb'] = draw
                df_league.loc[mask, 'HomeExp'] = exp1
                df_league.loc[mask, 'AwayExp'] = exp2

            if df_league.loc[mask, 'Result'].values[0] == "Draw":
                df_league.loc[mask, 'HomePoints'] = 1
                df_league.loc[mask, 'AwayPoints'] = 1
            elif df_league.loc[mask, 'Result'].values[0] == clubs[i]:
                df_league.loc[mask, 'HomePoints'] = 3
                df_league.loc[mask, 'AwayPoints'] = 0
            elif df_league.loc[mask, 'Result'].values[0] == clubs[j]:
                df_league.loc[mask, 'HomePoints'] = 0
                df_league.loc[mask, 'AwayPoints'] = 3

            # Autumn round
            win1, draw, win2, exp1, exp2 = match_score_propability(
                df_rating.loc[df_rating["Team"] == clubs[j], "Rating"].values[0],
                df_rating.loc[df_rating["Team"] == clubs[i], "Rating"].values[0],
                home_club_1=True,
                home_club_2=False
            )

            mask = df_league['Home'].eq(clubs[j]) & df_league['Away'].eq(clubs[i])
            if not pd.isna(df_league.loc[mask, "HomeGoals"].values[0]):
                if df_league.loc[mask, "HomeGoals"].values[0] > df_league.loc[mask, "AwayGoals"].values[0]:
                    df_league.loc[mask, 'Result'] = str(clubs[j]) # Home win
                elif df_league.loc[mask, "HomeGoals"].values[0] < df_league.loc[mask, "AwayGoals"].values[0]:
                    df_league.loc[mask, 'Result'] = str(clubs[i]) # Away win
                elif df_league.loc[mask, "HomeGoals"].values[0] == df_league.loc[mask, "AwayGoals"].values[0]:
                    df_league.loc[mask, 'Result'] = "Draw"  # Draw
                else:
                    df_league.loc[mask, 'Result'] = pd.NA,

            if pd.isna(df_league.loc[mask, "HomeGoals"].values[0]):
                df_league.loc[mask, 'HomeRating'] = df_rating.loc[df_rating["Team"] == clubs[j], "Rating"].values[0]
                df_league.loc[mask, 'AwayRating'] = df_rating.loc[df_rating["Team"] == clubs[i], "Rating"].values[0]
                df_league.loc[mask, 'HomeWinProb'] = win1
                df_league.loc[mask, 'AwayWinProb'] = win2
                df_league.loc[mask, 'DrawProb'] = draw
                df_league.loc[mask, 'HomeExp'] = exp1
                df_league.loc[mask, 'AwayExp'] = exp2

            if df_league.loc[mask, 'Result'].values[0] == "Draw":
                df_league.loc[mask, 'HomePoints'] = 1
                df_league.loc[mask, 'AwayPoints'] = 1
            elif df_league.loc[mask, 'Result'].values[0] == clubs[j]:
                df_league.loc[mask, 'HomePoints'] = 3
                df_league.loc[mask, 'AwayPoints'] = 0
            elif df_league.loc[mask, 'Result'].values[0] == clubs[i]:
                df_league.loc[mask, 'HomePoints'] = 0
                df_league.loc[mask, 'AwayPoints'] = 3

    return df_league

#PremierLegue:
df_rating = pd.read_excel(r"Data\data.xlsx")
df_league = pd.read_excel(rf"Sezon\{league_name_PremierLeague}.xlsx")

matches = matches_PremierLeague

for match in matches:
    add_match_result(df_league, match["match_week"], match["home"], match["home_goals"], match["away"], match["away_goals"],)

df_league = update_league(teams_PremierLeague, df_league)
df_league.to_excel(rf"Sezon\{league_name_PremierLeague}.xlsx", index=False)