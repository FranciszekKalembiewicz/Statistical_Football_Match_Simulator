import pandas as pd

league_name_Bundesliga = rf"Bundesliga2025_26"

teams_Bundesliga = pd.DataFrame({"Club": ["Bayern München","Borussia Dortmund","Bayer Leverkusen","RB Leipzig","Eintracht Frankfurt","Stuttgart","Freiburg","Werder Bremen","Hoffenheim","Mainz 05","Union Berlin","Borussia M'gladbach","Wolfsburg","Köln","Augsburg","Hamburger SV","St. Pauli","Heidenheim"]})

table_places_Bundesliga = {"win": [1], "champions_league": [1,2,3,4], "europa_league": [5], "conference_league": [6], "relegation": [16,17,18]}

matches_Bundesliga = [
    # Matchweek 1
    {"match_week": 1, "home": "Bayern Monachium", "home_goals": 6, "away": "RB Lipsk", "away_goals": 0},
    {"match_week": 1, "home": "Union Berlin", "home_goals": 2, "away": "VfB Stuttgart", "away_goals": 1},
    {"match_week": 1, "home": "SC Freiburg", "home_goals": 1, "away": "FC Augsburg", "away_goals": 3},
    {"match_week": 1, "home": "Heidenheim", "home_goals": 1, "away": "VfL Wolfsburg", "away_goals": 3},
    {"match_week": 1, "home": "Eintracht Frankfurt", "home_goals": 4, "away": "Werder Brema", "away_goals": 1},
    {"match_week": 1, "home": "Bayer Leverkusen", "home_goals": 1, "away": "TSG Hoffenheim", "away_goals": 2},
    {"match_week": 1, "home": "St. Pauli", "home_goals": 3, "away": "Borussia Dortmund", "away_goals": 3},
    {"match_week": 1, "home": "1. FSV Mainz 05", "home_goals": 0, "away": "1. FC Koeln", "away_goals": 1},
    {"match_week": 1, "home": "B. Moenchengladbach", "home_goals": 0, "away": "Hamburger SV", "away_goals": 0},

    # Matchweek 2
    {"match_week": 2, "home": "Hamburger SV", "home_goals": 0, "away": "St. Pauli", "away_goals": 2},
    {"match_week": 2, "home": "Werder Brema", "home_goals": 3, "away": "Bayer Leverkusen", "away_goals": 3},
    {"match_week": 2, "home": "VfB Stuttgart", "home_goals": 1, "away": "B. Moenchengladbach", "away_goals": 0},
    {"match_week": 2, "home": "TSG Hoffenheim", "home_goals": 1, "away": "Eintracht Frankfurt", "away_goals": 3},
    {"match_week": 2, "home": "RB Lipsk", "home_goals": 2, "away": "Heidenheim", "away_goals": 0},
    {"match_week": 2, "home": "FC Augsburg", "home_goals": 2, "away": "Bayern Monachium", "away_goals": 3},
    {"match_week": 2, "home": "VfL Wolfsburg", "home_goals": 1, "away": "1. FSV Mainz 05", "away_goals": 1},
    {"match_week": 2, "home": "Borussia Dortmund", "home_goals": 3, "away": "Union Berlin", "away_goals": 0},
    {"match_week": 2, "home": "1. FC Koeln", "home_goals": 4, "away": "SC Freiburg", "away_goals": 1},

    # Matchweek 3
    {"match_week": 3, "home": "Eintracht Frankfurt", "home_goals": 1, "away": "Borussia Dortmund", "away_goals": 2},
    {"match_week": 3, "home": "1. FC Koeln", "home_goals": 3, "away": "Bayer Leverkusen", "away_goals": 3},
    {"match_week": 3, "home": "TSG Hoffenheim", "home_goals": 4, "away": "VfL Wolfsburg", "away_goals": 3},
    {"match_week": 3, "home": "VfB Stuttgart", "home_goals": 1, "away": "Union Berlin", "away_goals": 2},
    {"match_week": 3, "home": "Borussia Dortmund", "home_goals": 2, "away": "SC Freiburg", "away_goals": 3},
    {"match_week": 3, "home": "RB Lipsk", "home_goals": 1, "away": "Heidenheim", "away_goals": 0},
    {"match_week": 3, "home": "Hamburger SV", "home_goals": 0, "away": "1. FSV Mainz 05", "away_goals": 0},
    {"match_week": 3, "home": "FC Augsburg", "home_goals": 1, "away": "Bayern Monachium", "away_goals": 5},
    {"match_week": 3, "home": "St. Pauli", "home_goals": 2, "away": "Werder Brema", "away_goals": 4},
    {"match_week": 3, "home": "B. Moenchengladbach", "home_goals": 0, "away": "VfL Wolfsburg", "away_goals": 1},

    # Matchweek 4
    {"match_week": 4, "home": "St. Pauli", "home_goals": 0, "away": "B. Moenchengladbach", "away_goals": 0},
    {"match_week": 4, "home": "SC Freiburg", "home_goals": 3, "away": "VfB Stuttgart", "away_goals": 2},
    {"match_week": 4, "home": "Bayern Monachium", "home_goals": 4, "away": "Werder Brema", "away_goals": 0},
    {"match_week": 4, "home": "Heidenheim", "home_goals": 1, "away": "TSG Hoffenheim", "away_goals": 1},
    {"match_week": 4, "home": "1. FSV Mainz 05", "home_goals": 4, "away": "Hamburger SV", "away_goals": 2},
    {"match_week": 4, "home": "1. FC Koeln", "home_goals": 1, "away": "FC Augsburg", "away_goals": 1},
    {"match_week": 4, "home": "RB Lipsk", "home_goals": 3, "away": "Union Berlin", "away_goals": 4},
    {"match_week": 4, "home": "Eintracht Frankfurt", "home_goals": 3, "away": "Bayer Leverkusen", "away_goals": 1},
    {"match_week": 4, "home": "Borussia Dortmund", "home_goals": 1, "away": "VfL Wolfsburg", "away_goals": 0},

    # Matchweek 5
    {"match_week": 5, "home": "Bayern Monachium", "home_goals": 4, "away": "Werder Brema", "away_goals": 0},
    {"match_week": 5, "home": "VfL Wolfsburg", "home_goals": 0, "away": "RB Lipsk", "away_goals": 1},
    {"match_week": 5, "home": "St. Pauli", "home_goals": 1, "away": "Bayer Leverkusen", "away_goals": 2},
    {"match_week": 5, "home": "Heidenheim", "home_goals": 2, "away": "FC Augsburg", "away_goals": 1},
    {"match_week": 5, "home": "1. FSV Mainz 05", "home_goals": 0, "away": "Borussia Dortmund", "away_goals": 2},
    {"match_week": 5, "home": "B. Moenchengladbach", "home_goals": 4, "away": "Eintracht Frankfurt", "away_goals": 6},
    {"match_week": 5, "home": "SC Freiburg", "home_goals": 1, "away": "TSG Hoffenheim", "away_goals": 1},
    {"match_week": 5, "home": "1. FC Koeln", "home_goals": 1, "away": "VfB Stuttgart", "away_goals": 2},
    {"match_week": 5, "home": "Union Berlin", "home_goals": 0, "away": "Hamburger SV", "away_goals": 0},

    # Matchweek 6
    {"match_week": 6, "home": "TSG Hoffenheim", "home_goals": 0, "away": "1. FC Koeln", "away_goals": 1},
    {"match_week": 6, "home": "Werder Brema", "home_goals": 1, "away": "St. Pauli", "away_goals": 0},
    {"match_week": 6, "home": "FC Augsburg", "home_goals": 3, "away": "VfL Wolfsburg", "away_goals": 1},
    {"match_week": 6, "home": "Borussia Dortmund", "home_goals": 1, "away": "RB Lipsk", "away_goals": 1},
    {"match_week": 6, "home": "Bayer Leverkusen", "home_goals": 2, "away": "Union Berlin", "away_goals": 0},
    {"match_week": 6, "home": "Eintracht Frankfurt", "home_goals": 0, "away": "Bayern Monachium", "away_goals": 3},
    {"match_week": 6, "home": "VfB Stuttgart", "home_goals": 1, "away": "Heidenheim", "away_goals": 0},
    {"match_week": 6, "home": "Hamburger SV", "home_goals": 4, "away": "1. FSV Mainz 05", "away_goals": 0},
    {"match_week": 6, "home": "B. Moenchengladbach", "home_goals": 0, "away": "SC Freiburg", "away_goals": 0},

    # Matchweek 7
    {"match_week": 7, "home": "Union Berlin", "home_goals": 3, "away": "VfB Stuttgart", "away_goals": 3},
    {"match_week": 7, "home": "Hamburger SV", "home_goals": 1, "away": "VfL Wolfsburg", "away_goals": 0},
    {"match_week": 7, "home": "RB Lipsk", "home_goals": 2, "away": "Werder Brema", "away_goals": 2},
    {"match_week": 7, "home": "Heidenheim", "home_goals": 2, "away": "Bayer Leverkusen", "away_goals": 4},
    {"match_week": 7, "home": "1. FSV Mainz 05", "home_goals": 3, "away": "FC Augsburg", "away_goals": 1},
    {"match_week": 7, "home": "1. FC Koeln", "home_goals": 1, "away": "Borussia Dortmund", "away_goals": 1},
    {"match_week": 7, "home": "Bayern Monachium", "home_goals": 2, "away": "Eintracht Frankfurt", "away_goals": 2},
    {"match_week": 7, "home": "SC Freiburg", "home_goals": 2, "away": "TSG Hoffenheim", "away_goals": 3},
    {"match_week": 7, "home": "St. Pauli", "home_goals": 0, "away": "Union Berlin", "away_goals": 0},

    # Matchweek 8
    {"match_week": 8, "home": "Werder Brema", "home_goals": 1, "away": "Heidenheim", "away_goals": 1},
    {"match_week": 8, "home": "Hamburger SV", "home_goals": 0, "away": "TSG Hoffenheim", "away_goals": 3},
    {"match_week": 8, "home": "VfL Wolfsburg", "home_goals": 1, "away": "RB Lipsk", "away_goals": 6},
    {"match_week": 8, "home": "FC Augsburg", "home_goals": 0, "away": "St. Pauli", "away_goals": 0},
    {"match_week": 8, "home": "Eintracht Frankfurt", "home_goals": 2, "away": "Hamburger SV", "away_goals": 0},
    {"match_week": 8, "home": "Bayern Monachium", "home_goals": 3, "away": "B. Moenchengladbach", "away_goals": 0},
    {"match_week": 8, "home": "Borussia Dortmund", "home_goals": 0, "away": "1. FC Koeln", "away_goals": 0},
    {"match_week": 8, "home": "Bayer Leverkusen", "home_goals": 2, "away": "SC Freiburg", "away_goals": 0},
    {"match_week": 8, "home": "VfB Stuttgart", "home_goals": 2, "away": "1. FSV Mainz 05", "away_goals": 1},

    # Matchweek 9
    {"match_week": 9, "home": "FC Augsburg", "home_goals": 0, "away": "Borussia Dortmund", "away_goals": 1},
    {"match_week": 9, "home": "Union Berlin", "home_goals": 0, "away": "SC Freiburg", "away_goals": 0},
    {"match_week": 9, "home": "St. Pauli", "home_goals": 0, "away": "B. Moenchengladbach", "away_goals": 4},
    {"match_week": 9, "home": "RB Lipsk", "home_goals": 3, "away": "VfB Stuttgart", "away_goals": 1},
    {"match_week": 9, "home": "Heidenheim", "home_goals": 1, "away": "Eintracht Frankfurt", "away_goals": 1},
    {"match_week": 9, "home": "1. FSV Mainz 05", "home_goals": 1, "away": "Werder Brema", "away_goals": 1},
    {"match_week": 9, "home": "Bayern Monachium", "home_goals": 3, "away": "Bayer Leverkusen", "away_goals": 0},
    {"match_week": 9, "home": "1. FC Koeln", "home_goals": 4, "away": "Hamburger SV", "away_goals": 1},
    {"match_week": 9, "home": "VfL Wolfsburg", "home_goals": 2, "away": "TSG Hoffenheim", "away_goals": 3},

    # Matchweek 10
    {"match_week": 10, "home": "Werder Brema", "home_goals": 2, "away": "VfL Wolfsburg", "away_goals": 1},
    {"match_week": 10, "home": "Union Berlin", "home_goals": 2, "away": "Bayern Monachium", "away_goals": 2},
    {"match_week": 10, "home": "TSG Hoffenheim", "home_goals": 3, "away": "RB Lipsk", "away_goals": 1},
    {"match_week": 10, "home": "Hamburger SV", "home_goals": 1, "away": "Borussia Dortmund", "away_goals": 1},
    {"match_week": 10, "home": "Bayer Leverkusen", "home_goals": 6, "away": "Heidenheim", "away_goals": 0},
    {"match_week": 10, "home": "B. Moenchengladbach", "home_goals": 3, "away": "1. FC Koeln", "away_goals": 1},
    {"match_week": 10, "home": "SC Freiburg", "home_goals": 2, "away": "St. Pauli", "away_goals": 1},
    {"match_week": 10, "home": "VfB Stuttgart", "home_goals": 3, "away": "FC Augsburg", "away_goals": 2},
    {"match_week": 10, "home": "Eintracht Frankfurt", "home_goals": 1, "away": "1. FSV Mainz 05", "away_goals": 0}
]