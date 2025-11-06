import numpy as np

def match_score_propability(rank_club_1, rank_club_2,home_club_1, home_club_2, draw_factor=0.73):
    # advantage of playing at home (sometimes both teams play away e.g. finals at neutral ground)
    if home_club_1:
        rank_club_1 += rank_club_1 / 25
    if home_club_2:
        rank_club_2 += rank_club_2 / 25

    # Logistic function to calculate win probabilities
    p_win_1 = 1 / (1 + np.exp(-(rank_club_1 - rank_club_2) / 7))
    p_win_2 = 1 - p_win_1
    p_draw = draw_factor * (1 - abs(p_win_1 - p_win_2))

    # Normalize probabilities to sum to 1
    total_prob = p_win_1 + p_win_2 + p_draw
    p_win_1 /= total_prob
    p_win_2 /= total_prob
    p_draw /= total_prob

    # Expected points
    p_exp_points_1 = p_win_1 * 3 + p_draw * 1 + p_win_2 * 0
    p_exp_points_2 = p_win_2 * 3 + p_draw * 1 + p_win_1 * 0

    return p_win_1, p_draw, p_win_2, p_exp_points_1, p_exp_points_2