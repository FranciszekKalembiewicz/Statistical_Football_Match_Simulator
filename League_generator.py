import pandas as pd
from Statistic_prediction import match_score_propability
from Matches.PremierLeague2025_26 import teams_PremierLeague, league_name_PremierLeague

df_rating = pd.read_excel(r"Data\data.xlsx")

def generate_matches_df(teams_df):
    clubs = teams_df["Club"].tolist()
    matches = []

    for i in range(len(clubs)):
        for j in range(i + 1, len(clubs)):

            # Spring round
            win1, draw, win2, exp1, exp2 = match_score_propability(
                df_rating.loc[df_rating["Team"] == clubs[i], "Rating"].values[0],
                df_rating.loc[df_rating["Team"] == clubs[j], "Rating"].values[0],
                home_club_1=True,
                home_club_2=False
            )

            matches.append({
                "MatchWeek": pd.NA,
                "Home": clubs[i],
                "Away": clubs[j],
                "HomeGoals": pd.NA,
                "AwayGoals": pd.NA,
                "Result": pd.NA,
                "HomeRating": df_rating.loc[df_rating["Team"] == clubs[i], "Rating"].values[0],
                "AwayRating": df_rating.loc[df_rating["Team"] == clubs[j], "Rating"].values[0],
                "HomeWinProb": win1,
                "AwayWinProb": win2,
                "DrawProb": draw,
                "HomeExp": exp1,
                "AwayExp": exp2,
                "HomePoints": pd.NA,
                "AwayPoints": pd.NA
            })

            # Autumn round
            win1, draw, win2, exp1, exp2 = match_score_propability(
                df_rating.loc[df_rating["Team"] == clubs[j], "Rating"].values[0],
                df_rating.loc[df_rating["Team"] == clubs[i], "Rating"].values[0],
                home_club_1=True,
                home_club_2=False
            )

            matches.append({
                "MatchWeek": pd.NA,
                "Home": clubs[j],
                "Away": clubs[i],
                "HomeGoals": pd.NA,
                "AwayGoals": pd.NA,
                "Result": pd.NA,
                "HomeRating": df_rating.loc[df_rating["Team"] == clubs[j], "Rating"].values[0],
                "AwayRating": df_rating.loc[df_rating["Team"] == clubs[i], "Rating"].values[0],
                "HomeWinProb": win1,
                "AwayWinProb": win2,
                "DrawProb": draw,
                "HomeExp": exp1,
                "AwayExp": exp2,
                "HomePoints": pd.NA,
                "AwayPoints": pd.NA
            })

    df_matches = pd.DataFrame(matches)
    return df_matches

#PremierLegue:
fixtures = generate_matches_df(teams_PremierLeague)
fixtures.to_excel(league_name_PremierLeague, index=False)
