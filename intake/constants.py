#KEYSPACE
#SEASON_SCHEMA
GAME_SCHEMA = { "table_name": "season_games",
  "options": {
    "primary_key": ["date", "w_team", "l_team"]
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
