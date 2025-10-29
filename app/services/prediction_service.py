import numpy as np

from app.schemas.prediction_schema import PredictionSchema
from app.services.stats_service import calculate_ratings, get_stats_for_team


def win_prediction_for_game(home_team: str, away_team: str):
    home_team_stats = get_stats_for_team(home_team)
    away_team_stats = get_stats_for_team(away_team)

    home_team_rating = calculate_ratings(home_team_stats["offense"],
                                         away_team_stats["defense"])

    away_team_rating = calculate_ratings(away_team_stats["offense"],
                                         home_team_stats["defense"])

    ratings = np.array([home_team_rating, away_team_rating])
    probabilities = ratings / ratings.sum()


    home_team_win_probability = float(max(min(probabilities[0], 0.95), 0.05))
    away_team_win_probability = float(max(min(probabilities[1], 0.95), 0.05))

    print(home_team_win_probability, away_team_win_probability)

    return PredictionSchema(home_team=home_team, away_team=away_team,
                            home_win_probability=round(home_team_win_probability, 2),
                            away_win_probability=round(away_team_win_probability, 2)
                            )
