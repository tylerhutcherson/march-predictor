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

  @staticmethod
  def record_games(games, skafos, batch_size):
    pass

  def get_game(self):
    return self.__dict__
