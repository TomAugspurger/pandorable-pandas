rest = teams.groupby('team')['date'].diff().dt.days - 1
rest
