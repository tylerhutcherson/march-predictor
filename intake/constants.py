KEYSPACE = "70c5a8c703cb0a81d2339171"

BATCH_SIZE = 10

SEASONS_SCHEMA = {
   "namespace": KEYSPACE,
   "table_name": "seaons",
   "options": {
     "primary_key": ["season"],
     "order_by": ["season desc"]
   },
  "columns": {
    "season": "int",
    "dayzero": "date",
    "regionx": "text",
    "regiony": "text",
    "regionw": "text",
    "regionz": "text"
  }
}

TEAMS_SCHEMA = {
  "namespace": KEYSPACE,
  "table_name": "teams",
  "options": {
    "primary_key": ["team_id"]
  },
  "columns": {
    "team_id": "text",
    "team_name": "text"
  }
}

TOURNEY_SCHEMA = {
  "namespace": KEYSPACE,
  "table_name": "games_tournament",
  "options": {
    "primary_key": ["date", "w_team", "l_team"],
    "order_by": ["date desc"]
  },
  "columns": {
     "w_team": "text",
     "l_team": "text",
     "season": "text",
     "date": "date",
     "location": "text",
     "numot": "int",
     "w_score": "int",
     "w_fgm": "int",
     "w_fga": "int",
     "w_3m": "int",
     "w_3a": "int",
     "w_ftm": "int",
     "w_fta": "int",
     "w_offreb": "int",
     "w_defreb": "int",
     "w_assists": "int",
     "w_turnovers": "int",
     "w_steals": "int",
     "w_blk": "int",
     "w_fouls": "int",
     "l_score": "int",
     "l_fgm": "int",
     "l_fga": "int",
     "l_3m": "int",
     "l_3a": "int",
     "l_ftm": "int",
     "l_fta": "int",
     "l_offreb": "int",
     "l_defreb": "int",
     "l_assists": "int",
     "l_turnovers": "int",
     "l_steals": "int",
     "l_blk": "int",
     "l_fouls": "int"
  }
 }

GAME_SCHEMA = { "namespace": KEYSPACE,
  "table_name": "games_reg_season",
  "options": {
    "primary_key": ["date", "w_team", "l_team"],
    "order_by": ["date desc"]
  },
  "columns": {
     "w_team": "text",
     "l_team": "text",
     "season": "text",
     "date": "date",
     "location": "text",
     "numot": "int",
     "w_score": "int",
     "w_fgm": "int",
     "w_fga": "int",
     "w_3m": "int",
     "w_3a": "int",
     "w_ftm": "int",
     "w_fta": "int",
     "w_offreb": "int",
     "w_defreb": "int",
     "w_assists": "int",
     "w_turnovers": "int",
     "w_steals": "int",
     "w_blk": "int",
     "w_fouls": "int",
     "l_score": "int",
     "l_fgm": "int",
     "l_fga": "int",
     "l_3m": "int",
     "l_3a": "int",
     "l_ftm": "int",
     "l_fta": "int",
     "l_offreb": "int",
     "l_defreb": "int",
     "l_assists": "int",
     "l_turnovers": "int",
     "l_steals": "int",
     "l_blk": "int",
     "l_fouls": "int"
  }
 }
