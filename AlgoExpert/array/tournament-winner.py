HOME_TEAM_WON = 1

def tournamentWinner(competitions, results):
    currentBestTeam = ""
    # scores dictionary to store each team and their points
    scores = {currentBestTeam: 0}

    # for loop to iterate through the competitions and results arrays
    # use the if statement to check if the current result is equal to 1
    # if it is, we will update the scores dictionary for the home team
    # otherwise, we will update the scores dictionary for the away team
    # also use the if statement to check if the current team has more points than the current best team
    # if it does, we will update the current best team
    # also use the if statement to check if the current team has the same points as the current best team
    for idx, competition in enumerate(competitions):
        result = results[idx]
        homeTeam, awayTeam = competition

        winningTeam = homeTeam if result == HOME_TEAM_WON else awayTeam

        updateScores(winningTeam, 3, scores)
        
        if scores[winningTeam] > scores[currentBestTeam]:
              currentBestTeam = winningTeam

    return currentBestTeam

# helper function to update the scores dictionary
# use the if statement to check if the current team is not in the scores dictionary
# if it is not, we will add the current team to the scores dictionary with the current points
# otherwise, we will update the current team's points in the scores dictionary
def updateScores(team, points, scores):
    if team not in scores:
        scores[team] = 0

    scores[team] += points
