home_more_rested = games_rest['home_rest'] > games_rest['away_rest']
home_won = games_rest['home_points'] > games_rest['away_points']
home_won.groupby(home_more_rested).mean()
