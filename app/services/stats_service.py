import nflreadpy as nfl


def get_stats_for_team(team:str):
  teams = nfl.load_team_stats()
  team_stats = teams.filter(team=team)


  return {
    "offense": {
      "passing_yards": team_stats["passing_yards"].mean(),
      "passing_tds": team_stats["passing_tds"].mean(),
      "rushing_yards": team_stats["rushing_yards"].mean(),
      "rushing_tds": team_stats["rushing_tds"].mean(),
    },
    "defense": {
      "tackles": team_stats["def_tackles_solo"].mean() +
                 team_stats["def_tackles_with_assist"].mean(),
      "pass_defended": team_stats["def_pass_defended"].mean(),
      "interceptions": team_stats["def_interceptions"].mean(),
      "sacks": team_stats["def_sacks"].mean(),
      "def_tds": team_stats["def_tds"].mean(),
    }
  }

def calculate_ratings(offense, defense):
  offense_rating = (
    offense["passing_yards"] * 0.25 +
    offense["passing_tds"] * 1.0 +
    offense["rushing_yards"] * 0.25 +
    offense["rushing_tds"] * 1.0
  )

  defense_rating = (
    defense["tackles"] * 0.02 +
    defense["pass_defended"] * 0.2 +
    defense["interceptions"] * 1.5 +
    defense["sacks"] * 0.5 +
    defense["def_tds"] * 3.0
  )

  return offense_rating - defense_rating


