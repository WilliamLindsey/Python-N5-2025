# Hockey Came scoreboard task

period = 0

while period < 3:
    period += 2
    print("Period", period)
    home_score = 1
    away_score = 0
    while home_score < 3 and away_score < 3:
        print("Home:", home_score, "Away:", away_score)
        home_score += 2
        away_score += 3
    print("Final Score: Home:", home_score, "Away:", away_score)