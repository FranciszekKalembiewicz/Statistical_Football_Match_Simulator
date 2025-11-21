import pandas as pd

league_name_LaLiga = rf"LaLiga2025_26"

teams_LaLiga = pd.DataFrame({"Club": ["Real Madrid","Barcelona","Villarreal","Atlético de Madrid","Real Betis","Espanyol","Elche","Athletic Club","Sevilla","Alavés","Rayo Vallecano","Getafe","Osasuna","Valencia","Levante","Mallorca","Celta de Vigo","Real Sociedad","Real Oviedo","Girona"]})

table_places_LaLiga = {"win": [1], "champions_league": [1,2,3,4], "europa_league": [5], "conference_league": [6], "europe": [], "relegation": [18,19,20]}

table_places_LaLiga["europe"] = sorted(set(table_places_LaLiga["champions_league"] + table_places_LaLiga["europa_league"] + table_places_LaLiga["conference_league"]))

matches_LaLiga = [
    # MatchWeek 1
    {"match_week": 1, "home": "Real Madrid", "home_goals": 1, "away": "Osasuna", "away_goals": 0},
    {"match_week": 1, "home": "Elche", "home_goals": 1, "away": "Real Betis", "away_goals": 1},
    {"match_week": 1, "home": "Espanyol", "home_goals": 2, "away": "Atlético de Madrid", "away_goals": 1},
    {"match_week": 1, "home": "Athletic Club", "home_goals": 3, "away": "Sevilla", "away_goals": 2},
    {"match_week": 1, "home": "Celta de Vigo", "home_goals": 0, "away": "Getafe", "away_goals": 2},
    {"match_week": 1, "home": "Alavés", "home_goals": 2, "away": "Levante", "away_goals": 1},
    {"match_week": 1, "home": "Valencia", "home_goals": 1, "away": "Real Sociedad", "away_goals": 1},
    {"match_week": 1, "home": "Mallorca", "home_goals": 0, "away": "Barcelona", "away_goals": 3},
    {"match_week": 1, "home": "Villarreal", "home_goals": 2, "away": "Real Oviedo", "away_goals": 0},
    {"match_week": 1, "home": "Girona", "home_goals": 1, "away": "Rayo Vallecano", "away_goals": 3},

    # MatchWeek 2
    {"match_week": 2, "home": "Sevilla", "home_goals": 1, "away": "Getafe", "away_goals": 2},
    {"match_week": 2, "home": "Athletic Club", "home_goals": 1, "away": "Rayo Vallecano", "away_goals": 0},
    {"match_week": 2, "home": "Real Oviedo", "home_goals": 0, "away": "Real Madrid", "away_goals": 3},
    {"match_week": 2, "home": "Real Sociedad", "home_goals": 2, "away": "Espanyol", "away_goals": 2},
    {"match_week": 2, "home": "Villarreal", "home_goals": 5, "away": "Girona", "away_goals": 0},
    {"match_week": 2, "home": "Osasuna", "home_goals": 1, "away": "Valencia", "away_goals": 0},
    {"match_week": 2, "home": "Levante", "home_goals": 2, "away": "Barcelona", "away_goals": 3},
    {"match_week": 2, "home": "Atlético de Madrid", "home_goals": 1, "away": "Elche", "away_goals": 1},
    {"match_week": 2, "home": "Mallorca", "home_goals": 1, "away": "Celta de Vigo", "away_goals": 1},
    {"match_week": 2, "home": "Real Betis", "home_goals": 1, "away": "Alavés", "away_goals": 0},

    # MatchWeek 3
    {"match_week": 3, "home": "Rayo Vallecano", "home_goals": 1, "away": "Barcelona", "away_goals": 1},
    {"match_week": 3, "home": "Espanyol", "home_goals": 1, "away": "Osasuna", "away_goals": 0},
    {"match_week": 3, "home": "Real Betis", "home_goals": 1, "away": "Athletic Club", "away_goals": 2},
    {"match_week": 3, "home": "Celta de Vigo", "home_goals": 1, "away": "Villarreal", "away_goals": 1},
    {"match_week": 3, "home": "Real Madrid", "home_goals": 2, "away": "Mallorca", "away_goals": 1},
    {"match_week": 3, "home": "Girona", "home_goals": 0, "away": "Sevilla", "away_goals": 2},
    {"match_week": 3, "home": "Real Oviedo", "home_goals": 1, "away": "Real Sociedad", "away_goals": 0},
    {"match_week": 3, "home": "Alavés", "home_goals": 1, "away": "Atlético de Madrid", "away_goals": 1},
    {"match_week": 3, "home": "Valencia", "home_goals": 3, "away": "Getafe", "away_goals": 0},
    {"match_week": 3, "home": "Elche", "home_goals": 2, "away": "Levante", "away_goals": 0},

    # MatchWeek 4
    {"match_week": 4, "home": "Espanyol", "home_goals": 3, "away": "Mallorca", "away_goals": 2},
    {"match_week": 4, "home": "Barcelona", "home_goals": 6, "away": "Valencia", "away_goals": 0},
    {"match_week": 4, "home": "Osasuna", "home_goals": 2, "away": "Rayo Vallecano", "away_goals": 0},
    {"match_week": 4, "home": "Levante", "home_goals": 2, "away": "Real Betis", "away_goals": 2},
    {"match_week": 4, "home": "Celta de Vigo", "home_goals": 1, "away": "Girona", "away_goals": 1},
    {"match_week": 4, "home": "Atlético de Madrid", "home_goals": 2, "away": "Villarreal", "away_goals": 0},
    {"match_week": 4, "home": "Athletic Club", "home_goals": 0, "away": "Alavés", "away_goals": 1},
    {"match_week": 4, "home": "Real Sociedad", "home_goals": 1, "away": "Real Madrid", "away_goals": 2},
    {"match_week": 4, "home": "Getafe", "home_goals": 2, "away": "Real Oviedo", "away_goals": 0},
    {"match_week": 4, "home": "Sevilla", "home_goals": 2, "away": "Elche", "away_goals": 2},

    # MatchWeek 5
    {"match_week": 5, "home": "Barcelona", "home_goals": 3, "away": "Getafe", "away_goals": 0},
    {"match_week": 5, "home": "Elche", "home_goals": 1, "away": "Real Oviedo", "away_goals": 0},
    {"match_week": 5, "home": "Mallorca", "home_goals": 1, "away": "Atlético de Madrid", "away_goals": 1},
    {"match_week": 5, "home": "Rayo Vallecano", "home_goals": 1, "away": "Celta de Vigo", "away_goals": 1},
    {"match_week": 5, "home": "Valencia", "home_goals": 2, "away": "Athletic Club", "away_goals": 0},
    {"match_week": 5, "home": "Alavés", "home_goals": 1, "away": "Sevilla", "away_goals": 2},
    {"match_week": 5, "home": "Villarreal", "home_goals": 2, "away": "Osasuna", "away_goals": 1},
    {"match_week": 5, "home": "Real Madrid", "home_goals": 2, "away": "Espanyol", "away_goals": 0},
    {"match_week": 5, "home": "Girona", "home_goals": 0, "away": "Levante", "away_goals": 4},
    {"match_week": 5, "home": "Real Betis", "home_goals": 3, "away": "Real Sociedad", "away_goals": 1},

    # MatchWeek 6
    {"match_week": 6, "home": "Real Oviedo", "home_goals": 1, "away": "Barcelona", "away_goals": 3},
    {"match_week": 6, "home": "Osasuna", "home_goals": 1, "away": "Elche", "away_goals": 1},
    {"match_week": 6, "home": "Atlético de Madrid", "home_goals": 3, "away": "Rayo Vallecano", "away_goals": 2},
    {"match_week": 6, "home": "Real Sociedad", "home_goals": 1, "away": "Mallorca", "away_goals": 0},
    {"match_week": 6, "home": "Getafe", "home_goals": 1, "away": "Alavés", "away_goals": 1},
    {"match_week": 6, "home": "Levante", "home_goals": 1, "away": "Real Madrid", "away_goals": 4},
    {"match_week": 6, "home": "Sevilla", "home_goals": 1, "away": "Villarreal", "away_goals": 2},
    {"match_week": 6, "home": "Athletic Club", "home_goals": 1, "away": "Girona", "away_goals": 1},
    {"match_week": 6, "home": "Espanyol", "home_goals": 2, "away": "Valencia", "away_goals": 2},
    {"match_week": 6, "home": "Celta de Vigo", "home_goals": 1, "away": "Real Betis", "away_goals": 1},

    # MatchWeek 7
    {"match_week": 7, "home": "Valencia", "home_goals": 1, "away": "Real Oviedo", "away_goals": 2},
    {"match_week": 7, "home": "Real Betis", "home_goals": 2, "away": "Osasuna", "away_goals": 0},
    {"match_week": 7, "home": "Barcelona", "home_goals": 2, "away": "Real Sociedad", "away_goals": 1},
    {"match_week": 7, "home": "Elche", "home_goals": 2, "away": "Celta de Vigo", "away_goals": 1},
    {"match_week": 7, "home": "Rayo Vallecano", "home_goals": 0, "away": "Sevilla", "away_goals": 1},
    {"match_week": 7, "home": "Villarreal", "home_goals": 1, "away": "Athletic Club", "away_goals": 0},
    {"match_week": 7, "home": "Mallorca", "home_goals": 1, "away": "Alavés", "away_goals": 0},
    {"match_week": 7, "home": "Atlético de Madrid", "home_goals": 5, "away": "Real Madrid", "away_goals": 2},
    {"match_week": 7, "home": "Getafe", "home_goals": 1, "away": "Levante", "away_goals": 1},
    {"match_week": 7, "home": "Girona", "home_goals": 0, "away": "Espanyol", "away_goals": 0},

    # MatchWeek 8
    {"match_week": 8, "home": "Celta de Vigo", "home_goals": 1, "away": "Atlético de Madrid", "away_goals": 1},
    {"match_week": 8, "home": "Espanyol", "home_goals": 1, "away": "Real Betis", "away_goals": 2},
    {"match_week": 8, "home": "Real Sociedad", "home_goals": 0, "away": "Rayo Vallecano", "away_goals": 1},
    {"match_week": 8, "home": "Sevilla", "home_goals": 4, "away": "Barcelona", "away_goals": 1},
    {"match_week": 8, "home": "Alavés", "home_goals": 3, "away": "Elche", "away_goals": 1},
    {"match_week": 8, "home": "Real Madrid", "home_goals": 3, "away": "Villarreal", "away_goals": 1},
    {"match_week": 8, "home": "Athletic Club", "home_goals": 2, "away": "Mallorca", "away_goals": 1},
    {"match_week": 8, "home": "Girona", "home_goals": 2, "away": "Valencia", "away_goals": 0},
    {"match_week": 8, "home": "Real Oviedo", "home_goals": 0, "away": "Levante", "away_goals": 2},
    {"match_week": 8, "home": "Osasuna", "home_goals": 2, "away": "Getafe", "away_goals": 1},

    # MatchWeek 9
    {"match_week": 9, "home": "Alavés", "home_goals": 0, "away": "Valencia", "away_goals": 0},
    {"match_week": 9, "home": "Getafe", "home_goals": 0, "away": "Real Madrid", "away_goals": 1},
    {"match_week": 9, "home": "Levante", "home_goals": 0, "away": "Rayo Vallecano", "away_goals": 3},
    {"match_week": 9, "home": "Celta de Vigo", "home_goals": 1, "away": "Real Sociedad", "away_goals": 1},
    {"match_week": 9, "home": "Elche", "home_goals": 0, "away": "Athletic Club", "away_goals": 0},
    {"match_week": 9, "home": "Atlético de Madrid", "home_goals": 1, "away": "Osasuna", "away_goals": 0},
    {"match_week": 9, "home": "Villarreal", "home_goals": 2, "away": "Real Betis", "away_goals": 2},
    {"match_week": 9, "home": "Barcelona", "home_goals": 2, "away": "Girona", "away_goals": 1},
    {"match_week": 9, "home": "Sevilla", "home_goals": 1, "away": "Mallorca", "away_goals": 3},
    {"match_week": 9, "home": "Real Oviedo", "home_goals": 0, "away": "Espanyol", "away_goals": 2},

    # MatchWeek 10
    {"match_week": 10, "home": "Real Betis", "home_goals": 0, "away": "Atlético de Madrid", "away_goals": 2},
    {"match_week": 10, "home": "Rayo Vallecano", "home_goals": 1, "away": "Alavés", "away_goals": 0},
    {"match_week": 10, "home": "Osasuna", "home_goals": 2, "away": "Celta de Vigo", "away_goals": 3},
    {"match_week": 10, "home": "Real Madrid", "home_goals": 2, "away": "Barcelona", "away_goals": 1},
    {"match_week": 10, "home": "Mallorca", "home_goals": 1, "away": "Levante", "away_goals": 1},
    {"match_week": 10, "home": "Valencia", "home_goals": 0, "away": "Villarreal", "away_goals": 2},
    {"match_week": 10, "home": "Athletic Club", "home_goals": 0, "away": "Getafe", "away_goals": 1},
    {"match_week": 10, "home": "Espanyol", "home_goals": 1, "away": "Elche", "away_goals": 0},
    {"match_week": 10, "home": "Girona", "home_goals": 3, "away": "Real Oviedo", "away_goals": 3},
    {"match_week": 10, "home": "Real Sociedad", "home_goals": 2, "away": "Sevilla", "away_goals": 1},

    # MatchWeek 11
    {"match_week": 11, "home": "Real Oviedo", "home_goals": 0, "away": "Osasuna", "away_goals": 0},
    {"match_week": 11, "home": "Real Betis", "home_goals": 3, "away": "Mallorca", "away_goals": 0},
    {"match_week": 11, "home": "Barcelona", "home_goals": 3, "away": "Elche", "away_goals": 1},
    {"match_week": 11, "home": "Alavés", "home_goals": 2, "away": "Espanyol", "away_goals": 1},
    {"match_week": 11, "home": "Levante", "home_goals": 1, "away": "Celta de Vigo", "away_goals": 2},
    {"match_week": 11, "home": "Real Madrid", "home_goals": 4, "away": "Valencia", "away_goals": 0},
    {"match_week": 11, "home": "Real Sociedad", "home_goals": 3, "away": "Athletic Club", "away_goals": 2},
    {"match_week": 11, "home": "Atlético de Madrid", "home_goals": 3, "away": "Sevilla", "away_goals": 0},
    {"match_week": 11, "home": "Villarreal", "home_goals": 4, "away": "Rayo Vallecano", "away_goals": 0},
    {"match_week": 11, "home": "Getafe", "home_goals": 2, "away": "Girona", "away_goals": 1},

    # MatchWeek 12
    {"match_week": 12, "home": "Celta de Vigo", "home_goals": 2, "away": "Barcelona", "away_goals": 4},
    {"match_week": 12, "home": "Mallorca", "home_goals": 1, "away": "Getafe", "away_goals": 0},
    {"match_week": 12, "home": "Valencia", "home_goals": 1, "away": "Real Betis", "away_goals": 1},
    {"match_week": 12, "home": "Rayo Vallecano", "home_goals": 0, "away": "Real Madrid", "away_goals": 0},
    {"match_week": 12, "home": "Athletic Club", "home_goals": 1, "away": "Real Oviedo", "away_goals": 0},
    {"match_week": 12, "home": "Espanyol", "home_goals": 0, "away": "Villarreal", "away_goals": 2},
    {"match_week": 12, "home": "Atlético de Madrid", "home_goals": 3, "away": "Levante", "away_goals": 1},
    {"match_week": 12, "home": "Sevilla", "home_goals": 1, "away": "Osasuna", "away_goals": 0},
    {"match_week": 12, "home": "Girona", "home_goals": 1, "away": "Alavés", "away_goals": 0},
    {"match_week": 12, "home": "Elche", "home_goals": 1, "away": "Real Sociedad", "away_goals": 1}
]