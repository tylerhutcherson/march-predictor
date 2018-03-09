# March Madness Bracket Predictor
Powered by Skafos - Machine Learning deployment automation by Metis Machine.

## Purpose
## Methodology
1. Data Sources
- The primary and starter source was the Kaggle dataset released for the March Machine Learning Mania 2016, 
ingested as a csv file. This is the base data that `game_ingester.py` augments daily using Skafos.
- Daily game outcomes are scraped from ___.
- Season statistics for each team are computed at the end of the regular season, prior to tournament action.

2. Data Schema
- Three tables were created to perform the modeling simulations with Skafos:\
**teams**: Table containing NCAA Men's Division 1 names and team IDs\
**season**: Table containing basic season information\
**season_games**: Table containing regular season game stats and outcomes\
```python
{ "table_name": "season_games",
  "options": {
    "primary_key": ["date", "w_team", "l_team"]
  },
  "columns": [
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
  ]
 }
```
**tournament**: Table containing tournament game outcomes\
{..}\
**statistics**: Table containing final season statistics for teams\
```python
{"team_id": "text",
 "season": "text",
 "total_wins": "int",
 "total_losses": "int",
 "avg_pnts": "float",
 "avg_pnts_alwd": "float",
 "avg_stealls": "float",
 "avg_turnovers": "float",
 "avg_blks": "float",
 "avg_assists": "float",
 "avg_offreb": "float",
 "avg_defreb": "float",
 "avg_fouls": "float",
 ...}
```
 

