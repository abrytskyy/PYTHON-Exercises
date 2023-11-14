#You have been provided with a data structure football_league, representing a season of a football league:

football_league = {
    "season": "2023",
    "teams": [
        {
            "name": "Team 1",
            "players": [
                {"name": "Player 1", "position": "Forward"},
                {"name": "Player 2", "position": "Defender"},
                {"name": "Player 3", "position": "Goalkeeper"},
            ],
            "results": [
                {"opponent": "Team 2", "score": "2:1"},
                {"opponent": "Team 3", "score": "3:0"},
                {"opponent": "Team 4", "score": "1:1"},
            ],
        },
        {
            "name": "Team 2",
            "players": [
                {"name": "Player 4", "position": "Forward"},
                {"name": "Player 5", "position": "Defender"},
                {"name": "Player 6", "position": "Goalkeeper"},
            ],
            "results": [
                {"opponent": "Team 1", "score": "1:2"},
                {"opponent": "Team 3", "score": "0:0"},
                {"opponent": "Team 4", "score": "2:1"},
            ],
        },
        {
            "name": "Team 3",
            "players": [
                {"name": "Player 7", "position": "Forward"},
                {"name": "Player 8", "position": "Defender"},
                {"name": "Player 9", "position": "Goalkeeper"},
            ],
            "results": [
                {"opponent": "Team 1", "score": "0:3"},
                {"opponent": "Team 2", "score": "0:0"},
                {"opponent": "Team 4", "score": "2:2"},
            ],
        },
        {
            "name": "Team 4",
            "players": [
                {"name": "Player 10", "position": "Forward"},
                {"name": "Player 11", "position": "Defender"},
                {"name": "Player 12", "position": "Goalkeeper"},
            ],
            "results": [
                {"opponent": "Team 1", "score": "1:1"},
                {"opponent": "Team 2", "score": "1:2"},
                {"opponent": "Team 3", "score": "2:2"},
            ],
        },
    ],
}

#You need to develop a Python program that allows you to perform the following operations:
#1. Display the overall season results, including information about teams, their players, and
# the results of each team in all matches.
def print_season_result(footbal_league):
    print(f"Season: {football_league['season']}\n")
    print(f'Teams: \n')
    for team in footbal_league["teams"]:
        print(team["name"])
        print("Players: ")
        for player in team["players"]:
            print(player)
        print("Results: ")
        for result in team["results"]:
            print(result)
        print()
        print()
print_season_result(football_league)

#2. Calculate the total number of wins, draws, and losses for each team.
def total_win_draw_losses_by_team(footbal_league):

    win_draw_losses = {}
    for team in footbal_league["teams"]:
        team_name = team["name"]
        results = team["results"]
        wins = 0
        draws = 0
        losses = 0

        for result in results:
            score = result["score"]
            own_score,oponent_score = map(int, score.split(":"))
            if own_score > oponent_score:
                wins += 1
            elif own_score == oponent_score:
                draws += 1
            else:
                losses += 1

        win_draw_losses[team_name] = wins, draws, losses
    print("Team *: (win,draw,loss)")
    print(win_draw_losses)
    print()

#another output, each team from new line:
    print("Team * (win,draw,loss)")
    for team,result in win_draw_losses.items():
        print(team,result)

total_win_draw_losses_by_team(football_league)

#3. Determine the team with the highest number of wins in the season.
def max_wins():
    return max(total_win_draw_losses_by_team, key=lambda x: x[1])


#4. Determine the top goal scorer (player with the highest number of goals).

#5. Determine the team with the highest number of goals scored.

#6. Determine the team with the fewest goals conceded.

#7. Display the average result in all matches of the season.

#8. Calculate the total number of goals scored and conceded in the season.

#9. Display a table of results sorted by the number of points earned (3 points for a win, 1 for a draw, 0 for a loss).

#10. Display the match schedule for each team.

#11. Calculate the average number of goals in each match of the season.

#12. Calculate the percentage of wins, draws, and losses for each team.

#13. Display a list of players who have scored at least one goal.