import pandas as pd

league_name_Bundesliga = rf"Bundesliga2025_26"

teams_Bundesliga = pd.DataFrame({"Club": ["Bayern München","Borussia Dortmund","Bayer Leverkusen","RB Leipzig","Eintracht Frankfurt","Stuttgart","Freiburg","Werder Bremen","Hoffenheim","Mainz 05","Union Berlin","Borussia M'gladbach","Wolfsburg","Köln","Augsburg","Hamburger SV","St. Pauli","Heidenheim"]})

table_places_Bundesliga = {"win": [1], "champions_league": [1,2,3,4], "europa_league": [5], "conference_league": [6], "europe": [], "relegation": [16,17,18]}

table_places_Bundesliga["europe"] = sorted(set(table_places_Bundesliga["champions_league"] + table_places_Bundesliga["europa_league"] + table_places_Bundesliga["conference_league"]))

matches_Bundesliga = [
    # Matchweek 1
    {"match_week": 1, "home": "Bayern München", "home_goals": 6, "away": "RB Leipzig", "away_goals": 0},
    {"match_week": 1, "home": "Union Berlin", "home_goals": 2, "away": "Stuttgart", "away_goals": 1},
    {"match_week": 1, "home": "Freiburg", "home_goals": 1, "away": "Augsburg", "away_goals": 3},
    {"match_week": 1, "home": "Heidenheim", "home_goals": 1, "away": "Wolfsburg", "away_goals": 3},
    {"match_week": 1, "home": "Eintracht Frankfurt", "home_goals": 4, "away": "Werder Brema", "away_goals": 1},
    {"match_week": 1, "home": "Bayer Leverkusen", "home_goals": 1, "away": "Hoffenheim", "away_goals": 2},
    {"match_week": 1, "home": "St. Pauli", "home_goals": 3, "away": "Borussia Dortmund", "away_goals": 3},
    {"match_week": 1, "home": "Mainz 05", "home_goals": 0, "away": "Köln", "away_goals": 1},
    {"match_week": 1, "home": "B. M'gladbach", "home_goals": 0, "away": "Hamburger SV", "away_goals": 0},

    # Matchweek 2
    {"match_week": 2, "home": "Köln", "home_goals": 4, "away": "Freiburg", "away_goals": 1},
    {"match_week": 2, "home": "Borussia Dortmund", "home_goals": 3, "away": "Union Berlin", "away_goals": 0},
    {"match_week": 2, "home": "Wolfsburg", "home_goals": 1, "away": "Mainz 05", "away_goals": 1},
    {"match_week": 2, "home": "Augsburg", "home_goals": 2, "away": "Bayern München", "away_goals": 3},
    {"match_week": 2, "home": "RB Leipzig", "home_goals": 2, "away": "Heidenheim", "away_goals": 0},
    {"match_week": 2, "home": "Hoffenheim", "home_goals": 1, "away": "Eintracht Frankfurt", "away_goals": 3},
    {"match_week": 2, "home": "Stuttgart", "home_goals": 1, "away": "B. M'gladbach", "away_goals": 0},
    {"match_week": 2, "home": "Werder Brema", "home_goals": 3, "away": "Bayer Leverkusen", "away_goals": 3},
    {"match_week": 2, "home": "Hamburger SV", "home_goals": 0, "away": "St. Pauli", "away_goals": 2},

    # Matchweek 3
    {"match_week": 3, "home": "B. M'gladbach", "home_goals": 0, "away": "Werder Brema", "away_goals": 4},
    {"match_week": 3, "home": "St. Pauli", "home_goals": 2, "away": "Augsburg", "away_goals": 1},
    {"match_week": 3, "home": "Bayern München", "home_goals": 5, "away": "Hamburger SV", "away_goals": 0},
    {"match_week": 3, "home": "Mainz 05", "home_goals": 0, "away": "RB Leipzig", "away_goals": 1},
    {"match_week": 3, "home": "Heidenheim", "home_goals": 0, "away": "Borussia Dortmund", "away_goals": 2},
    {"match_week": 3, "home": "Freiburg", "home_goals": 3, "away": "Stuttgart", "away_goals": 1},
    {"match_week": 3, "home": "Union Berlin", "home_goals": 2, "away": "Hoffenheim", "away_goals": 1},
    {"match_week": 3, "home": "Wolfsburg", "home_goals": 3, "away": "Köln", "away_goals": 3},
    {"match_week": 3, "home": "Bayer Leverkusen", "home_goals": 2, "away": "Eintracht Frankfurt", "away_goals": 3},

    # Matchweek 4
    {"match_week": 4, "home": "Borussia Dortmund", "home_goals": 1, "away": "Wolfsburg", "away_goals": 0},
    {"match_week": 4, "home": "Bayer Leverkusen", "home_goals": 1, "away": "B. M'gladbach", "away_goals": 1},
    {"match_week": 4, "home": "Eintracht Frankfurt", "home_goals": 3, "away": "Union Berlin", "away_goals": 4},
    {"match_week": 4, "home": "RB Leipzig", "home_goals": 3, "away": "Köln", "away_goals": 1},
    {"match_week": 4, "home": "Augsburg", "home_goals": 1, "away": "Mainz 05", "away_goals": 4},
    {"match_week": 4, "home": "Hamburger SV", "home_goals": 2, "away": "Heidenheim", "away_goals": 1},
    {"match_week": 4, "home": "Hoffenheim", "home_goals": 1, "away": "Bayern München", "away_goals": 4},
    {"match_week": 4, "home": "Werder Brema", "home_goals": 0, "away": "Freiburg", "away_goals": 3},
    {"match_week": 4, "home": "Stuttgart", "home_goals": 2, "away": "St. Pauli", "away_goals": 1},

    # Matchweek 5
    {"match_week": 5, "home": "Bayern München", "home_goals": 4, "away": "Werder Brema", "away_goals": 0},
    {"match_week": 5, "home": "Wolfsburg", "home_goals": 0, "away": "RB Leipzig", "away_goals": 1},
    {"match_week": 5, "home": "St. Pauli", "home_goals": 1, "away": "Bayer Leverkusen", "away_goals": 2},
    {"match_week": 5, "home": "Heidenheim", "home_goals": 2, "away": "Augsburg", "away_goals": 1},
    {"match_week": 5, "home": "Mainz 05", "home_goals": 0, "away": "Borussia Dortmund", "away_goals": 2},
    {"match_week": 5, "home": "B. M'gladbach", "home_goals": 4, "away": "Eintracht Frankfurt", "away_goals": 6},
    {"match_week": 5, "home": "Freiburg", "home_goals": 1, "away": "Hoffenheim", "away_goals": 1},
    {"match_week": 5, "home": "Köln", "home_goals": 1, "away": "Stuttgart", "away_goals": 2},
    {"match_week": 5, "home": "Union Berlin", "home_goals": 0, "away": "Hamburger SV", "away_goals": 0},

    # Matchweek 6
    {"match_week": 6, "home": "B. M'gladbach", "home_goals": 0, "away": "Freiburg", "away_goals": 0},
    {"match_week": 6, "home": "Hamburger SV", "home_goals": 4, "away": "Mainz 05", "away_goals": 0},
    {"match_week": 6, "home": "Stuttgart", "home_goals": 1, "away": "Heidenheim", "away_goals": 0},
    {"match_week": 6, "home": "Eintracht Frankfurt", "home_goals": 0, "away": "Bayern München", "away_goals": 3},
    {"match_week": 6, "home": "Bayer Leverkusen", "home_goals": 2, "away": "Union Berlin", "away_goals": 0},
    {"match_week": 6, "home": "Borussia Dortmund", "home_goals": 1, "away": "RB Leipzig", "away_goals": 1},
    {"match_week": 6, "home": "Augsburg", "home_goals": 3, "away": "Wolfsburg", "away_goals": 1},
    {"match_week": 6, "home": "Werder Brema", "home_goals": 1, "away": "St. Pauli", "away_goals": 0},
    {"match_week": 6, "home": "Hoffenheim", "home_goals": 0, "away": "Köln", "away_goals": 1},

    # Matchweek 7
    {"match_week": 7, "home": "St. Pauli", "home_goals": 0, "away": "Stuttgart", "away_goals": 3},
    {"match_week": 7, "home": "Freiburg", "home_goals": 2, "away": "Eintracht Frankfurt", "away_goals": 2},
    {"match_week": 7, "home": "Bayern München", "home_goals": 2, "away": "Borussia Dortmund", "away_goals": 1},
    {"match_week": 7, "home": "Köln", "home_goals": 1, "away": "Augsburg", "away_goals": 1},
    {"match_week": 7, "home": "Mainz 05", "home_goals": 3, "away": "Bayer Leverkusen", "away_goals": 4},
    {"match_week": 7, "home": "Heidenheim", "home_goals": 2, "away": "Werder Brema", "away_goals": 2},
    {"match_week": 7, "home": "RB Leipzig", "home_goals": 2, "away": "Hamburger SV", "away_goals": 1},
    {"match_week": 7, "home": "Wolfsburg", "home_goals": 0, "away": "Stuttgart", "away_goals": 3},
    {"match_week": 7, "home": "Union Berlin", "home_goals": 3, "away": "B. M'gladbach", "away_goals": 1},

    # Matchweek 8
    {"match_week": 8, "home": "Stuttgart", "home_goals": 2, "away": "Mainz 05", "away_goals": 1},
    {"match_week": 8, "home": "Bayer Leverkusen", "home_goals": 2, "away": "Freiburg", "away_goals": 0},
    {"match_week": 8, "home": "Borussia Dortmund", "home_goals": 1, "away": "Köln", "away_goals": 0},
    {"match_week": 8, "home": "B. M'gladbach", "home_goals": 0, "away": "Bayern München", "away_goals": 3},
    {"match_week": 8, "home": "Eintracht Frankfurt", "home_goals": 2, "away": "St. Pauli", "away_goals": 0},
    {"match_week": 8, "home": "Augsburg", "home_goals": 0, "away": "RB Leipzig", "away_goals": 6},
    {"match_week": 8, "home": "Hamburger SV", "home_goals": 0, "away": "Wolfsburg", "away_goals": 1},
    {"match_week": 8, "home": "Hoffenheim", "home_goals": 3, "away": "Heidenheim", "away_goals": 1},
    {"match_week": 8, "home": "Werder Brema", "home_goals": 1, "away": "Union Berlin", "away_goals": 0},

    # Matchweek 9
    {"match_week": 9, "home": "Wolfsburg", "home_goals": 2, "away": "Hoffenheim", "away_goals": 3},
    {"match_week": 9, "home": "Köln", "home_goals": 4, "away": "Hamburger SV", "away_goals": 1},
    {"match_week": 9, "home": "Bayern München", "home_goals": 3, "away": "Bayer Leverkusen", "away_goals": 0},
    {"match_week": 9, "home": "Mainz 05", "home_goals": 1, "away": "Werder Brema", "away_goals": 1},
    {"match_week": 9, "home": "Heidenheim", "home_goals": 1, "away": "Eintracht Frankfurt", "away_goals": 1},
    {"match_week": 9, "home": "RB Leipzig", "home_goals": 3, "away": "Stuttgart", "away_goals": 1},
    {"match_week": 9, "home": "St. Pauli", "home_goals": 0, "away": "B. M'gladbach", "away_goals": 4},
    {"match_week": 9, "home": "Union Berlin", "home_goals": 0, "away": "Freiburg", "away_goals": 0},
    {"match_week": 9, "home": "Augsburg", "home_goals": 0, "away": "Borussia Dortmund", "away_goals": 1},

    # Matchweek 10
    {"match_week": 10, "home": "Eintracht Frankfurt", "home_goals": 1, "away": "Mainz 05", "away_goals": 0},
    {"match_week": 10, "home": "Stuttgart", "home_goals": 3, "away": "Augsburg", "away_goals": 2},
    {"match_week": 10, "home": "Freiburg", "home_goals": 2, "away": "St. Pauli", "away_goals": 1},
    {"match_week": 10, "home": "B. M'gladbach", "home_goals": 3, "away": "Köln", "away_goals": 1},
    {"match_week": 10, "home": "Bayer Leverkusen", "home_goals": 6, "away": "Heidenheim", "away_goals": 0},
    {"match_week": 10, "home": "Hamburger SV", "home_goals": 1, "away": "Borussia Dortmund", "away_goals": 1},
    {"match_week": 10, "home": "Hoffenheim", "home_goals": 3, "away": "RB Leipzig", "away_goals": 1},
    {"match_week": 10, "home": "Union Berlin", "home_goals": 2, "away": "Bayern München", "away_goals": 2},
    {"match_week": 10, "home": "Werder Brema", "home_goals": 2, "away": "Wolfsburg", "away_goals": 1}
]