import pandas as pd

league_name_PremierLeague = rf"Sezon\PremierLeague2025_26.xlsx"

teams_PremierLeague = pd.DataFrame({"Club": ["Arsenal","Manchester City","Liverpool","AFC Bournemouth","Chelsea","Tottenham Hotspur","Sunderland","Crystal Palace","Manchester United","Brighton & Hove Albion","Aston Villa","Everton","Newcastle United","Fulham","Leeds United","Brentford","Burnley","Nottingham Forest","West Ham United","Wolverhampton Wanderers"]})

matches_PremierLeague = [
    # MatchWeek 1
    {"match_week": 1, "home": "Liverpool", "home_goals": 4, "away": "AFC Bournemouth", "away_goals": 2},
    {"match_week": 1, "home": "Aston Villa", "home_goals": 0, "away": "Newcastle United", "away_goals": 0},
    {"match_week": 1, "home": "Tottenham Hotspur", "home_goals": 3, "away": "Burnley", "away_goals": 0},
    {"match_week": 1, "home": "Sunderland", "home_goals": 3, "away": "West Ham United", "away_goals": 0},
    {"match_week": 1, "home": "Brighton & Hove Albion", "home_goals": 1, "away": "Fulham", "away_goals": 1},
    {"match_week": 1, "home": "Wolverhampton Wanderers", "home_goals": 0, "away": "Manchester City", "away_goals": 4},
    {"match_week": 1, "home": "Nottingham Forest", "home_goals": 3, "away": "Brentford", "away_goals": 1},
    {"match_week": 1, "home": "Chelsea", "home_goals": 0, "away": "Crystal Palace", "away_goals": 0},
    {"match_week": 1, "home": "Manchester United", "home_goals": 0, "away": "Arsenal", "away_goals": 1},
    {"match_week": 1, "home": "Leeds United", "home_goals": 1, "away": "Everton", "away_goals": 0},

    # MatchWeek 2
    {"match_week": 2, "home": "West Ham United", "home_goals": 1, "away": "Chelsea", "away_goals": 5},
    {"match_week": 2, "home": "Manchester City", "home_goals": 0, "away": "Tottenham Hotspur", "away_goals": 2},
    {"match_week": 2, "home": "Burnley", "home_goals": 2, "away": "Sunderland", "away_goals": 0},
    {"match_week": 2, "home": "Brentford", "home_goals": 1, "away": "Aston Villa", "away_goals": 0},
    {"match_week": 2, "home": "AFC Bournemouth", "home_goals": 1, "away": "Wolverhampton Wanderers", "away_goals": 0},
    {"match_week": 2, "home": "Everton", "home_goals": 2, "away": "Brighton & Hove Albion", "away_goals": 0},
    {"match_week": 2, "home": "Crystal Palace", "home_goals": 1, "away": "Nottingham Forest", "away_goals": 1},
    {"match_week": 2, "home": "Fulham", "home_goals": 1, "away": "Manchester United", "away_goals": 1},
    {"match_week": 2, "home": "Arsenal", "home_goals": 5, "away": "Leeds United", "away_goals": 0},
    {"match_week": 2, "home": "Newcastle United", "home_goals": 2, "away": "Liverpool", "away_goals": 3},

    # MatchWeek 3
    {"match_week": 3, "home": "Chelsea", "home_goals": 2, "away": "Fulham", "away_goals": 0},
    {"match_week": 3, "home": "Wolverhampton Wanderers", "home_goals": 2, "away": "Everton", "away_goals": 2},
    {"match_week": 3, "home": "Tottenham Hotspur", "home_goals": 0, "away": "AFC Bournemouth", "away_goals": 1},
    {"match_week": 3, "home": "Sunderland", "home_goals": 2, "away": "Brentford", "away_goals": 1},
    {"match_week": 3, "home": "Burnley", "home_goals": 2, "away": "Manchester United", "away_goals": 3},
    {"match_week": 3, "home": "Leeds United", "home_goals": 0, "away": "Newcastle United", "away_goals": 0},
    {"match_week": 3, "home": "Nottingham Forest", "home_goals": 0, "away": "West Ham United", "away_goals": 3},
    {"match_week": 3, "home": "Brighton & Hove Albion", "home_goals": 2, "away": "Manchester City", "away_goals": 1},
    {"match_week": 3, "home": "Liverpool", "home_goals": 1, "away": "Arsenal", "away_goals": 0},
    {"match_week": 3, "home": "Aston Villa", "home_goals": 0, "away": "Crystal Palace", "away_goals": 3},

    # MatchWeek 4
    {"match_week": 4, "home": "Arsenal", "home_goals": 3, "away": "Nottingham Forest", "away_goals": 0},
    {"match_week": 4, "home": "Newcastle United", "home_goals": 1, "away": "Wolverhampton Wanderers", "away_goals": 0},
    {"match_week": 4, "home": "Fulham", "home_goals": 1, "away": "Leeds United", "away_goals": 0},
    {"match_week": 4, "home": "Everton", "home_goals": 0, "away": "Aston Villa", "away_goals": 0},
    {"match_week": 4, "home": "Crystal Palace", "home_goals": 0, "away": "Sunderland", "away_goals": 0},
    {"match_week": 4, "home": "AFC Bournemouth", "home_goals": 2, "away": "Brighton & Hove Albion", "away_goals": 1},
    {"match_week": 4, "home": "West Ham United", "home_goals": 0, "away": "Tottenham Hotspur", "away_goals": 3},
    {"match_week": 4, "home": "Brentford", "home_goals": 2, "away": "Chelsea", "away_goals": 2},
    {"match_week": 4, "home": "Burnley", "home_goals": 0, "away": "Liverpool", "away_goals": 1},
    {"match_week": 4, "home": "Manchester City", "home_goals": 3, "away": "Manchester United", "away_goals": 0},

    # MatchWeek 5
    {"match_week": 5, "home": "Liverpool", "home_goals": 2, "away": "Everton", "away_goals": 1},
    {"match_week": 5, "home": "Wolverhampton Wanderers", "home_goals": 1, "away": "Leeds United", "away_goals": 3},
    {"match_week": 5, "home": "West Ham United", "home_goals": 1, "away": "Crystal Palace", "away_goals": 2},
    {"match_week": 5, "home": "Burnley", "home_goals": 1, "away": "Nottingham Forest", "away_goals": 1},
    {"match_week": 5, "home": "Brighton & Hove Albion", "home_goals": 2, "away": "Tottenham Hotspur", "away_goals": 2},
    {"match_week": 5, "home": "Manchester United", "home_goals": 2, "away": "Chelsea", "away_goals": 1},
    {"match_week": 5, "home": "Fulham", "home_goals": 3, "away": "Brentford", "away_goals": 1},
    {"match_week": 5, "home": "Sunderland", "home_goals": 1, "away": "Aston Villa", "away_goals": 1},
    {"match_week": 5, "home": "AFC Bournemouth", "home_goals": 0, "away": "Newcastle United", "away_goals": 0},
    {"match_week": 5, "home": "Arsenal", "home_goals": 1, "away": "Manchester City", "away_goals": 1},

    # MatchWeek 6
    {"match_week": 6, "home": "Brentford", "home_goals": 3, "away": "Manchester United", "away_goals": 1},
    {"match_week": 6, "home": "Manchester City", "home_goals": 5, "away": "Burnley", "away_goals": 1},
    {"match_week": 6, "home": "Leeds United", "home_goals": 2, "away": "AFC Bournemouth", "away_goals": 2},
    {"match_week": 6, "home": "Crystal Palace", "home_goals": 2, "away": "Liverpool", "away_goals": 1},
    {"match_week": 6, "home": "Chelsea", "home_goals": 1, "away": "Brighton & Hove Albion", "away_goals": 3},
    {"match_week": 6, "home": "Nottingham Forest", "home_goals": 0, "away": "Sunderland", "away_goals": 1},
    {"match_week": 6, "home": "Tottenham Hotspur", "home_goals": 1, "away": "Wolverhampton Wanderers", "away_goals": 1},
    {"match_week": 6, "home": "Aston Villa", "home_goals": 3, "away": "Fulham", "away_goals": 1},
    {"match_week": 6, "home": "Newcastle United", "home_goals": 1, "away": "Arsenal", "away_goals": 2},
    {"match_week": 6, "home": "Everton", "home_goals": 1, "away": "West Ham United", "away_goals": 1},

    # MatchWeek 7
    {"match_week": 7, "home": "AFC Bournemouth", "home_goals": 3, "away": "Fulham", "away_goals": 1},
    {"match_week": 7, "home": "Leeds United", "home_goals": 1, "away": "Tottenham Hotspur", "away_goals": 1},
    {"match_week": 7, "home": "Manchester United", "home_goals": 2, "away": "Sunderland", "away_goals": 2},
    {"match_week": 7, "home": "Arsenal", "home_goals": 2, "away": "West Ham United", "away_goals": 0},
    {"match_week": 7, "home": "Chelsea", "home_goals": 2, "away": "Liverpool", "away_goals": 1},
    {"match_week": 7, "home": "Wolverhampton Wanderers", "home_goals": 1, "away": "Brighton & Hove Albion", "away_goals": 1},
    {"match_week": 7, "home": "Newcastle United", "home_goals": 2, "away": "Nottingham Forest", "away_goals": 1},
    {"match_week": 7, "home": "Everton", "home_goals": 2, "away": "Crystal Palace", "away_goals": 1},
    {"match_week": 7, "home": "Aston Villa", "home_goals": 2, "away": "Burnley", "away_goals": 1},
    {"match_week": 7, "home": "Brentford", "home_goals": 0, "away": "Manchester City", "away_goals": 1},

    # MatchWeek 8
    {"match_week": 8, "home": "Nottingham Forest", "home_goals": 0, "away": "Chelsea", "away_goals": 3},
    {"match_week": 8, "home": "Sunderland", "home_goals": 0, "away": "Wolverhampton Wanderers", "away_goals": 0},
    {"match_week": 8, "home": "Manchester City", "home_goals": 2, "away": "Everton", "away_goals": 1},
    {"match_week": 8, "home": "Crystal Palace", "home_goals": 3, "away": "AFC Bournemouth", "away_goals": 3},
    {"match_week": 8, "home": "Burnley", "home_goals": 2, "away": "Leeds United", "away_goals": 0},
    {"match_week": 8, "home": "Brighton & Hove Albion", "home_goals": 2, "away": "Newcastle United", "away_goals": 1},
    {"match_week": 8, "home": "Fulham", "home_goals": 0, "away": "Arsenal", "away_goals": 2},
    {"match_week": 8, "home": "Tottenham Hotspur", "home_goals": 1, "away": "Aston Villa", "away_goals": 2},
    {"match_week": 8, "home": "Liverpool", "home_goals": 1, "away": "Manchester United", "away_goals": 2},
    {"match_week": 8, "home": "West Ham United", "home_goals": 0, "away": "Brentford", "away_goals": 2},

]