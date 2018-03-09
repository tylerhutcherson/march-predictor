# Dump starter data to skafos tables
import os
import pandas as pd
from datetime import timedelta
from game import Game, write_data
from skafossdk import *

ska = Skafos()


## Variables
# Location of initial datasets
DATA_PREFIX = "/home/tchutch/Documents/datasets/march_madness/"

# Load Data from disk
seasons = pd.read_csv(DATA_PREFIX + "Seasons.csv")
games = pd.read_csv(DATA_PREFIX + "RegularSeasonDetailedResults.csv")
teams = pd.read_csv(DATA_PREFIX + "Teams.csv")
tourney = pd.read_csv(DATA_PREFIX + "TourneyDetailedResults.csv")

# Merge and Cleaning
seasons = seasons[['Season', 'Dayzero']]
seasons['Dayzero'] = seasons.Dayzero.apply(lambda x: pd.to_datetime(x))
games_ext = seasons.merge(games, on='Season', how='right')
games_ext['date'] = games_ext.apply(lambda r: r.Dayzero + timedelta(days=r.Daynum), axis=1)
tourney_ext = seasons.merge(tourney, on='Season', how='right')
tourney_ext['date'] = tourney_ext.apply(lambda r: r.Dayzero + timedelta(days=r.Daynum), axis=1)
teams.columns = ['team_id', 'team_name']
seasons.columns = ['season', 'dayzero']

# Make games dataset
print("Preparing regular season game data")
games_data = []
for i, r in games_ext.iterrows():
  games_data.append(Game(r).get_game())

print("Preparing tournament data")
tourney_data = []
for i, r in tourney_ext.iterrows():
  tourney_data.append(Game(r).get_game())

# Write data to cassandra using Skafos Data Engine
print("Writing data to cassandra tables", flush=True)
write_data(games_data, ska.engine, GAME_SCHEMA, BATCH_SIZE)
write_data(tourney_data, ska.engine, TOURNEY_SCHEMA, BATCH_SIZE)
write_data(seasons.to_dict('records'), ska.engine, SEASONS_SCHEMA, BATCH_SIZE)
write_data(teams.to_dict('records'), ska.engine, TEAMS_SCHEMA, BATCH_SIZE)
print("Done.", flush=True)