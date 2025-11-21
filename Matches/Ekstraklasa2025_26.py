import pandas as pd

league_name_Ekstraklasa = rf"Ekstraklasa2025_26"

teams_Ekstraklasa = pd.DataFrame({"Club": ["Lech Poznań","Raków Częstochowa","Jagiellonia Białystok","Pogoń Szczecin","Legia Warszawa","Cracovia","Motor Lublin","GKS Katowice","Górnik Zabrze","Piast Gliwice","Korona Kielce","Radomiak Radom","Widzew Łódź","Lechia Gdańsk","Zagłębie Lubin","Wisła Płock","Arka Gdynia","Nieciecza"]})

table_places_Ekstraklasa = {"win": [1], "champions_league": [1,2], "europa_league": [], "conference_league": [3,4], "europe": [], "relegation": [16,17,18]}

table_places_Ekstraklasa["europe"] = sorted(set(table_places_Ekstraklasa["champions_league"] + table_places_Ekstraklasa["europa_league"] + table_places_Ekstraklasa["conference_league"]))

matches_Ekstraklasa = [
    # MatchWeek 1
    {"match_week": 1, "home": "Radomiak Radom", "home_goals": 5, "away": "Pogoń Szczecin", "away_goals": 1},
    {"match_week": 1, "home": "Motor Lublin", "home_goals": 1, "away": "Arka Gdynia", "away_goals": 0},
    {"match_week": 1, "home": "Górnik Zabrze", "home_goals": 2, "away": "Lechia Gdańsk", "away_goals": 1},
    {"match_week": 1, "home": "GKS Katowice", "home_goals": 0, "away": "Raków Częstochowa", "away_goals": 1},
    {"match_week": 1, "home": "Wisła Płock", "home_goals": 2, "away": "Korona Kielce", "away_goals": 0},
    {"match_week": 1, "home": "Widzew Łódź", "home_goals": 1, "away": "Zagłębie Lubin", "away_goals": 0},
    {"match_week": 1, "home": "Lech Poznań", "home_goals": 1, "away": "Cracovia", "away_goals": 4},
    {"match_week": 1, "home": "Jagiellonia Białystok", "home_goals": 0, "away": "Nieciecza", "away_goals": 4},

    # MatchWeek 2
    {"match_week": 2, "home": "GKS Katowice", "home_goals": 2, "away": "Zagłębie Lubin", "away_goals": 2},
    {"match_week": 2, "home": "Korona Kielce", "home_goals": 0, "away": "Legia Warszawa", "away_goals": 2},
    {"match_week": 2, "home": "Jagiellonia Białystok", "home_goals": 3, "away": "Widzew Łódź", "away_goals": 2},
    {"match_week": 2, "home": "Raków Częstochowa", "home_goals": 1, "away": "Wisła Płock", "away_goals": 2},
    {"match_week": 2, "home": "Lechia Gdańsk", "home_goals": 3, "away": "Lech Poznań", "away_goals": 4},
    {"match_week": 2, "home": "Pogoń Szczecin", "home_goals": 4, "away": "Motor Lublin", "away_goals": 1},
    {"match_week": 2, "home": "Piast Gliwice", "home_goals": 0, "away": "Górnik Zabrze", "away_goals": 1},
    {"match_week": 2, "home": "Arka Gdynia", "home_goals": 1, "away": "Radomiak Radom", "away_goals": 1},
    {"match_week": 2, "home": "Cracovia", "home_goals": 2, "away": "Nieciecza", "away_goals": 0},

    # MatchWeek 3
    {"match_week": 3, "home": "Legia Warszawa", "home_goals": 0, "away": "Arka Gdynia", "away_goals": 0},
    {"match_week": 3, "home": "Radomiak Radom", "home_goals": 3, "away": "Raków Częstochowa", "away_goals": 1},
    {"match_week": 3, "home": "Cracovia", "home_goals": 2, "away": "Lechia Gdańsk", "away_goals": 2},
    {"match_week": 3, "home": "Lech Poznań", "home_goals": 2, "away": "Górnik Zabrze", "away_goals": 1},
    {"match_week": 3, "home": "Widzew Łódź", "home_goals": 3, "away": "GKS Katowice", "away_goals": 0},
    {"match_week": 3, "home": "Nieciecza", "home_goals": 1, "away": "Pogoń Szczecin", "away_goals": 1},
    {"match_week": 3, "home": "Wisła Płock", "home_goals": 2, "away": "Piast Gliwice", "away_goals": 0},
    {"match_week": 3, "home": "Zagłębie Lubin", "home_goals": 1, "away": "Korona Kielce", "away_goals": 1},
    {"match_week": 3, "home": "Motor Lublin", "home_goals": 0, "away": "Jagiellonia Białystok", "away_goals": 2},

    # MatchWeek 4
    {"match_week": 4, "home": "Lechia Gdańsk", "home_goals": 3, "away": "Motor Lublin", "away_goals": 3},
    {"match_week": 4, "home": "Legia Warszawa", "home_goals": 3, "away": "GKS Katowice", "away_goals": 1},
    {"match_week": 4, "home": "Jagiellonia Białystok", "home_goals": 5, "away": "Cracovia", "away_goals": 2},
    {"match_week": 4, "home": "Widzew Łódź", "home_goals": 1, "away": "Wisła Płock", "away_goals": 1},
    {"match_week": 4, "home": "Arka Gdynia", "home_goals": 2, "away": "Pogoń Szczecin", "away_goals": 1},
    {"match_week": 4, "home": "Górnik Zabrze", "home_goals": 0, "away": "Nieciecza", "away_goals": 1},
    {"match_week": 4, "home": "Korona Kielce", "home_goals": 3, "away": "Radomiak Radom", "away_goals": 0},
    {"match_week": 4, "home": "Piast Gliwice", "home_goals": 0, "away": "Lech Poznań", "away_goals": 0},

    # MatchWeek 5
    {"match_week": 5, "home": "Nieciecza", "home_goals": 2, "away": "Raków Częstochowa", "away_goals": 3},
    {"match_week": 5, "home": "Wisła Płock", "home_goals": 1, "away": "Legia Warszawa", "away_goals": 0},
    {"match_week": 5, "home": "Pogoń Szczecin", "home_goals": 0, "away": "Górnik Zabrze", "away_goals": 3},
    {"match_week": 5, "home": "Radomiak Radom", "home_goals": 1, "away": "Jagiellonia Białystok", "away_goals": 2},
    {"match_week": 5, "home": "Lech Poznań", "home_goals": 1, "away": "Korona Kielce", "away_goals": 1},
    {"match_week": 5, "home": "GKS Katowice", "home_goals": 4, "away": "Arka Gdynia", "away_goals": 1},
    {"match_week": 5, "home": "Motor Lublin", "home_goals": 0, "away": "Piast Gliwice", "away_goals": 0},
    {"match_week": 5, "home": "Cracovia", "home_goals": 1, "away": "Widzew Łódź", "away_goals": 0},
    {"match_week": 5, "home": "Zagłębie Lubin", "home_goals": 6, "away": "Lechia Gdańsk", "away_goals": 2},

    # MatchWeek 6
    {"match_week": 6, "home": "Wisła Płock", "home_goals": 2, "away": "Zagłębie Lubin", "away_goals": 1},
    {"match_week": 6, "home": "Lechia Gdańsk", "home_goals": 1, "away": "Arka Gdynia", "away_goals": 0},
    {"match_week": 6, "home": "Piast Gliwice", "home_goals": 0, "away": "Cracovia", "away_goals": 0},
    {"match_week": 6, "home": "Górnik Zabrze", "home_goals": 3, "away": "GKS Katowice", "away_goals": 0},
    {"match_week": 6, "home": "Korona Kielce", "home_goals": 2, "away": "Motor Lublin", "away_goals": 0},
    {"match_week": 6, "home": "Widzew Łódź", "home_goals": 1, "away": "Pogoń Szczecin", "away_goals": 2},
    {"match_week": 6, "home": "Radomiak Radom", "home_goals": 1, "away": "Nieciecza", "away_goals": 1},
    {"match_week": 6, "home": "Legia Warszawa", "home_goals": 0, "away": "Jagiellonia Białystok", "away_goals": 0},
    {"match_week": 6, "home": "Raków Częstochowa", "home_goals": 2, "away": "Lech Poznań", "away_goals": 0},

    # MatchWeek 7
    {"match_week": 7, "home": "Cracovia", "home_goals": 2, "away": "Legia Warszawa", "away_goals": 1},
    {"match_week": 7, "home": "Pogoń Szczecin", "home_goals": 2, "away": "Raków Częstochowa", "away_goals": 0},
    {"match_week": 7, "home": "Jagiellonia Białystok", "home_goals": 2, "away": "Lechia Gdańsk", "away_goals": 0},
    {"match_week": 7, "home": "Lech Poznań", "home_goals": 2, "away": "Widzew Łódź", "away_goals": 1},
    {"match_week": 7, "home": "Górnik Zabrze", "home_goals": 0, "away": "Motor Lublin", "away_goals": 1},
    {"match_week": 7, "home": "Zagłębie Lubin", "home_goals": 2, "away": "Piast Gliwice", "away_goals": 2},
    {"match_week": 7, "home": "Nieciecza", "home_goals": 1, "away": "Korona Kielce", "away_goals": 3},
    {"match_week": 7, "home": "GKS Katowice", "home_goals": 3, "away": "Radomiak Radom", "away_goals": 2},
    {"match_week": 7, "home": "Arka Gdynia", "home_goals": 1, "away": "Wisła Płock", "away_goals": 0},

    # MatchWeek 8
    {"match_week": 8, "home": "Raków Częstochowa", "home_goals": 0, "away": "Górnik Zabrze", "away_goals": 1},
    {"match_week": 8, "home": "Widzew Łódź", "home_goals": 2, "away": "Arka Gdynia", "away_goals": 0},
    {"match_week": 8, "home": "Legia Warszawa", "home_goals": 4, "away": "Radomiak Radom", "away_goals": 1},
    {"match_week": 8, "home": "Motor Lublin", "home_goals": 1, "away": "Nieciecza", "away_goals": 1},
    {"match_week": 8, "home": "Piast Gliwice", "home_goals": 1, "away": "Jagiellonia Białystok", "away_goals": 1},
    {"match_week": 8, "home": "Korona Kielce", "home_goals": 1, "away": "Pogoń Szczecin", "away_goals": 0},
    {"match_week": 8, "home": "Lech Poznań", "home_goals": 1, "away": "Zagłębie Lubin", "away_goals": 2},
    {"match_week": 8, "home": "Lechia Gdańsk", "home_goals": 2, "away": "GKS Katowice", "away_goals": 0},

    # MatchWeek 9
    {"match_week": 9, "home": "Górnik Zabrze", "home_goals": 3, "away": "Widzew Łódź", "away_goals": 2},
    {"match_week": 9, "home": "Pogoń Szczecin", "home_goals": 3, "away": "Lechia Gdańsk", "away_goals": 4},
    {"match_week": 9, "home": "Zagłębie Lubin", "home_goals": 2, "away": "Motor Lublin", "away_goals": 2},
    {"match_week": 9, "home": "Raków Częstochowa", "home_goals": 1, "away": "Legia Warszawa", "away_goals": 0},
    {"match_week": 9, "home": "Nieciecza", "home_goals": 0, "away": "Lech Poznań", "away_goals": 2},
    {"match_week": 9, "home": "Arka Gdynia", "home_goals": 0, "away": "Korona Kielce", "away_goals": 0},
    {"match_week": 9, "home": "Radomiak Radom", "home_goals": 1, "away": "Piast Gliwice", "away_goals": 0},
    {"match_week": 9, "home": "Wisła Płock", "home_goals": 0, "away": "Jagiellonia Białystok", "away_goals": 1},
    {"match_week": 9, "home": "GKS Katowice", "home_goals": 1, "away": "Cracovia", "away_goals": 3},

    # MatchWeek 10
    {"match_week": 10, "home": "Motor Lublin", "home_goals": 2, "away": "Radomiak Radom", "away_goals": 2},
    {"match_week": 10, "home": "Zagłębie Lubin", "home_goals": 4, "away": "Arka Gdynia", "away_goals": 0},
    {"match_week": 10, "home": "Legia Warszawa", "home_goals": 1, "away": "Pogoń Szczecin", "away_goals": 0},
    {"match_week": 10, "home": "Lech Poznań", "home_goals": 2, "away": "Jagiellonia Białystok", "away_goals": 2},
    {"match_week": 10, "home": "Widzew Łódź", "home_goals": 2, "away": "Raków Częstochowa", "away_goals": 1},
    {"match_week": 10, "home": "Cracovia", "home_goals": 1, "away": "Górnik Zabrze", "away_goals": 1},
    {"match_week": 10, "home": "Piast Gliwice", "home_goals": 4, "away": "Nieciecza", "away_goals": 2},
    {"match_week": 10, "home": "Korona Kielce", "home_goals": 3, "away": "Lechia Gdańsk", "away_goals": 0},
    {"match_week": 10, "home": "Wisła Płock", "home_goals": 1, "away": "GKS Katowice", "away_goals": 1},

    # MatchWeek 11
    {"match_week": 11, "home": "Górnik Zabrze", "home_goals": 3, "away": "Legia Warszawa", "away_goals": 1},
    {"match_week": 11, "home": "GKS Katowice", "home_goals": 1, "away": "Lech Poznań", "away_goals": 0},
    {"match_week": 11, "home": "Raków Częstochowa", "home_goals": 2, "away": "Motor Lublin", "away_goals": 0},
    {"match_week": 11, "home": "Jagiellonia Białystok", "home_goals": 3, "away": "Korona Kielce", "away_goals": 1},
    {"match_week": 11, "home": "Arka Gdynia", "home_goals": 2, "away": "Cracovia", "away_goals": 1},
    {"match_week": 11, "home": "Radomiak Radom", "home_goals": 3, "away": "Zagłębie Lubin", "away_goals": 1},
    {"match_week": 11, "home": "Nieciecza", "home_goals": 2, "away": "Widzew Łódź", "away_goals": 4},
    {"match_week": 11, "home": "Pogoń Szczecin", "home_goals": 2, "away": "Piast Gliwice", "away_goals": 1},
    {"match_week": 11, "home": "Lechia Gdańsk", "home_goals": 1, "away": "Wisła Płock", "away_goals": 1},

    # MatchWeek 12
    {"match_week": 12, "home": "Wisła Płock", "home_goals": 3, "away": "Nieciecza", "away_goals": 1},
    {"match_week": 12, "home": "Zagłębie Lubin", "home_goals": 3, "away": "Legia Warszawa", "away_goals": 1},
    {"match_week": 12, "home": "Lech Poznań", "home_goals": 2, "away": "Pogoń Szczecin", "away_goals": 2},
    {"match_week": 12, "home": "Piast Gliwice", "home_goals": 1, "away": "Lechia Gdańsk", "away_goals": 2},
    {"match_week": 12, "home": "Cracovia", "home_goals": 2, "away": "Raków Częstochowa", "away_goals": 0},
    {"match_week": 12, "home": "Jagiellonia Białystok", "home_goals": 4, "away": "Arka Gdynia", "away_goals": 0},
    {"match_week": 12, "home": "Korona Kielce", "home_goals": 1, "away": "Górnik Zabrze", "away_goals": 1},
    {"match_week": 12, "home": "Widzew Łódź", "home_goals": 3, "away": "Radomiak Radom", "away_goals": 2},
    {"match_week": 12, "home": "Motor Lublin", "home_goals": 2, "away": "GKS Katowice", "away_goals": 5},

    # MatchWeek 13
    {"match_week": 13, "home": "Radomiak Radom", "home_goals": 1, "away": "Wisła Płock", "away_goals": 1},
    {"match_week": 13, "home": "Legia Warszawa", "home_goals": 0, "away": "Lech Poznań", "away_goals": 0},
    {"match_week": 13, "home": "Górnik Zabrze", "home_goals": 2, "away": "Jagiellonia Białystok", "away_goals": 1},
    {"match_week": 13, "home": "Raków Częstochowa", "home_goals": 2, "away": "Lechia Gdańsk", "away_goals": 1},
    {"match_week": 13, "home": "GKS Katowice", "home_goals": 1, "away": "Korona Kielce", "away_goals": 0},
    {"match_week": 13, "home": "Pogoń Szczecin", "home_goals": 2, "away": "Cracovia", "away_goals": 1},
    {"match_week": 13, "home": "Arka Gdynia", "home_goals": 2, "away": "Piast Gliwice", "away_goals": 1},
    {"match_week": 13, "home": "Motor Lublin", "home_goals": 3, "away": "Widzew Łódź", "away_goals": 0},
    {"match_week": 13, "home": "Nieciecza", "home_goals": 1, "away": "Zagłębie Lubin", "away_goals": 1},

    # MatchWeek 14
    {"match_week": 14, "home": "Cracovia", "home_goals": 0, "away": "Zagłębie Lubin", "away_goals": 0},
    {"match_week": 14, "home": "Lechia Gdańsk", "home_goals": 1, "away": "Radomiak Radom", "away_goals": 2},
    {"match_week": 14, "home": "Wisła Płock", "home_goals": 2, "away": "Pogoń Szczecin", "away_goals": 0},
    {"match_week": 14, "home": "Widzew Łódź", "home_goals": 1, "away": "Legia Warszawa", "away_goals": 1},
    {"match_week": 14, "home": "Jagiellonia Białystok", "home_goals": 1, "away": "Raków Częstochowa", "away_goals": 2},
    {"match_week": 14, "home": "Lech Poznań", "home_goals": 2, "away": "Motor Lublin", "away_goals": 2},
    {"match_week": 14, "home": "Górnik Zabrze", "home_goals": 5, "away": "Arka Gdynia", "away_goals": 1},
    {"match_week": 14, "home": "Piast Gliwice", "home_goals": 0, "away": "Korona Kielce", "away_goals": 0},
    {"match_week": 14, "home": "Nieciecza", "home_goals": 0, "away": "GKS Katowice", "away_goals": 3},

    # MatchWeek 15
    {"match_week": 15, "home": "Arka Gdynia", "home_goals": 3, "away": "Lech Poznań", "away_goals": 1},
    {"match_week": 15, "home": "Pogoń Szczecin", "home_goals": 1, "away": "Jagiellonia Białystok", "away_goals": 2},
    {"match_week": 15, "home": "Korona Kielce", "home_goals": 1, "away": "Raków Częstochowa", "away_goals": 4},
    {"match_week": 15, "home": "Legia Warszawa", "home_goals": 1, "away": "Nieciecza", "away_goals": 2},
    {"match_week": 15, "home": "GKS Katowice", "home_goals": 1, "away": "Piast Gliwice", "away_goals": 3},
    {"match_week": 15, "home": "Motor Lublin", "home_goals": 1, "away": "Wisła Płock", "away_goals": 1},
    {"match_week": 15, "home": "Lechia Gdańsk", "home_goals": 2, "away": "Widzew Łódź", "away_goals": 1},
    {"match_week": 15, "home": "Zagłębie Lubin", "home_goals": 2, "away": "Górnik Zabrze", "away_goals": 0},
    {"match_week": 15, "home": "Radomiak Radom", "home_goals": 3, "away": "Cracovia", "away_goals": 0}
]