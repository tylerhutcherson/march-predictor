from constants import *
import pandas as pd


GAME_FIELDS = list(GAME_SCHEMA['columns'].keys())


class Game(object):

  def __init__(self, r):
    """Basic game level characteristics"""
    self.w_team = r.Wteam
    self.l_team = r.Lteam
    self.season = int(r.Season)
    self.date = pd.to_datetime(r.date)
    self.location = self.w_team if r.Wloc == 'H' else (self.l_team if r.Wloc == 'A' else r.Wloc)
    self.numot = int(r.Numot)
    self.w_score = r.Wscore
    self.w_fgm = r.Wfgm
    self.w_fga = r.Wfga
    self.w_3m = r.Wfgm3
    self.w_3a = r.Wfga3
    self.w_ftm = r.Wftm
    self.w_fta = r.Wfta
    self.w_offreb = r.Wor
    self.w_defreb = r.Wdr
    self.w_assists = r.Wast
    self.w_turnovers = r.Wto
    self.w_steals = r.Wstl
    self.w_blk = r.Wblk
    self.w_fouls = r.Wpf
    self.l_score = r.Lscore
    self.l_fgm = r.Lfgm
    self.l_fga = r.Lfga
    self.l_m3 = r.Lfgm3
    self.l_a3 = r.Lfga3
    self.l_ftm = r.Lftm
    self.l_fta = r.Lfta
    self.l_offreb = r.Lor
    self.l_defreb = r.Ldr
    self.l_assists = r.Last
    self.l_turnovers = r.Lto
    self.l_steals = r.Last
    self.l_blk = r.Lblk
    self.l_fouls = r.Lpf

  @property
  def get_stat(self, arg):
    return self.__dict__[arg]

  @property
  def get_game(self):
    return self.__dict__


class Season(object):

  def __init__(self, skafos, season, team_id=None, team_name=None):
    self.ska = skafos
    if team_name and not team_id:
      res = self.ska.engine.create_view(
          "teams", {"keyspace": KEYSPACE,
          "table": "teams"}, DataSourceType.Cassandra).result()
      teams = self.ska.engine.query("SELECT team_id FROM teams where team_name = {}".format(team_name)).result()
      if 'data' in teams:
        self.team_id = teams['data'].get('team_id')
      else:
        sys.exit("Unknown team name entered or Data Engine Failure.")
    elif team_id:
      self.team_id = team_id
    else:
      sys.exit("Must provide either team_id or team_name")
    self.season = int(season
    # TODO figure this out
   # self.stats = {
   # win_count = 0
   # loss_count = 0
   # fgm = 0
   # ftm = 0
   # fga = 0
   # fta = 0
   # made3 = 0
   # att3 = 0
   # steals = 0
   # blks = 0
   # offreb = 0
   # defreb = 0
   # points = 0
   # points_allwd = 0
   # numot = 0
   # turnovers = 0
   # }

  def _get_team_season_stats(self):
    res = self.ska.engine.create_view(
        "games", {"keyspace": KEYSPACE,
        "table": "games_reg_season"}, DataSourceType.Cassandra).result()
    game_query = "SELECT * FROM games WHERE w_team={} OR  l_team={} AND season={}".format((self.team_id, self.team_id, self.season))
    self.season = self.ska.engine.query(game_query).result()['data']
    # Go through each game of the regular season and create stats summary
    for game in self.season:
      if game.get('w_team') == self.team_id:
        status = 'w'
        win_count += 1
        self._augment_stats(status, game)  # this would augment team stats for season with this game
      else:
        status = 'l'
        loss_count += 1

  # TODO make this guy
  def _augment_stats(self, status, game):
    #self.stats
    pass


def write_data(data, engine, schema, batch_size):
  """Write batches of data to data engine."""
  for rows in batches(data, batch_size):
    res = engine.save(schema, list(rows)).result()


def batches(iterable, n):
  """Divide a single list into a list of lists of size n"""
  batchLen = len(iterable)
  for ndx in range(0, batchLen, n):
    yield list(iterable[ndx:min(ndx + n, batchLen)])
