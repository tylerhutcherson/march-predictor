CREATE KEYSPACE "70c5a8c703cb0a81d2339171"
  WITH REPLICATION = {
   'class' : 'SimpleStrategy',
   'replication_factor' : 3
  };

-- Regular Season Games
CREATE TABLE "70c5a8c703cb0a81d2339171".games_reg_season (
  w_team text,
  l_team text,
  season int,
  date date,
  location text,
  numot int,
  w_score int,
  w_fgm int,
  w_fga int,
  w_3m int,
  w_3a int,
  w_ftm int,
  w_fta int,
  w_offreb int,
  w_defreb int,
  w_assists int,
  w_turnovers int,
  w_steals int,
  w_blk int,
  w_fouls int,
  l_score int,
  l_fgm int,
  l_fga int,
  l_3m int,
  l_3a int,
  l_ftm int,
  l_fta int,
  l_offreb int,
  l_defreb int,
  l_assists int,
  l_turnovers int,
  l_steals int,
  l_blk int,
  l_fouls int,
  PRIMARY KEY (date, w_team, l_team)
) WITH CLUSTERING ORDER BY (date DESC);

-- Tournament Games
CREATE TABLE "70c5a8c703cb0a81d2339171".games_tournament (
  w_team text,
  l_team text,
  season int,
  date date,
  location text,
  numot int,
  w_score int,
  w_fgm int,
  w_fga int,
  w_3m int,
  w_3a int,
  w_ftm int,
  w_fta int,
  w_offreb int,
  w_defreb int,
  w_assists int,
  w_turnovers int,
  w_steals int,
  w_blk int,
  w_fouls int,
  l_score int,
  l_fgm int,
  l_fga int,
  l_3m int,
  l_3a int,
  l_ftm int,
  l_fta int,
  l_offreb int,
  l_defreb int,
  l_assists int,
  l_turnovers int,
  l_steals int,
  l_blk int,
  l_fouls int,
  PRIMARY KEY (date, w_team, l_team)
) WITH CLUSTERING ORDER BY (date DESC);

-- NCAA Division 1 Teams
CREATE TABLE "70c5a8c703cb0a81d2339171".teams (
  team_id text,
  team_name text,
  PRIMARY KEY (team_id)
);

-- Basketball Seasons
CREATE TABLE "70c5a8c703cb0a81d2339171".seasons (
  season int,
  dayzero date,
  regionx text,
  regiony text,
  regionw text,
  regionz text,
  PRIMARY KEY (season)
) WITH CLUSTERING ORDER BY (season DESC);
