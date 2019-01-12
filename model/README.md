# March Madness Model Doc

Goal: Given information about the opposing teams, matchup, and intangibles,
      predict the likelihood of team A beating team B.


Model Style: Classification


Features:
  -  Regular Season Data (for Team A and Team B)
      -  Non-Conference Period
      -  Conference Part 1
      -  Conference Part 2
  -  Tournament Team Health
      -  Major Player Missing (y/n)
      -  Minor Player Missing (y/n)
  -  Tournament History
      -  Titles in Last 10 Years
      -  Performance vs. Expectation in Last 10 Years
      -  Hall of Fame Coach (y/n)
  -  Matchup
      -  Seeds, AP Rank, RPI, BPI, Kenpom (Margin? or Raw?)
      -  Location Proximity to "Home Base"
      -  Tournament Historical Results (based on seed)


