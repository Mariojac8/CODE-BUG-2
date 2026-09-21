# DEBUGGING CHALLENGE
team_name = "Wildcats"

wins = 12
losses = 4

games_played = wins + losses 

win_percentages = wins / games_played 

if win_percentages >= .58: 
    print(team_name, "are likely to make the playoffs!") 
else: 
    print(team_name, "needs to win more games.")

    print("team:", team_name) 

    if wins > 10: 
        print("winning season!")

        def winning_record(wins,losses): 
            return wins > losses 

        result = winning_record(wins,losses) 

        print("winning Record?", result) 

        #print GAMES PLAYED AND WIN PERCENTAGE 
        print("games played", games_played) 
        print("win percentage:", win_percentages)
        print("win percentage:", round win_percentages)
