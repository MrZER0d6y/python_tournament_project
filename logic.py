from mock_data import *
from games import ranking_table
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

def leading_team():
    if matches == []:
        print("")
        loggin.warning("No games were played.\n")
        return
    
    table = ranking_table()
    print(f"The leading team: {table[0]["name"]}")
    print("")
    logging.info("leading team were printed.\n")
    return

def best_attacking_team():
    best_teams = []
    highest = []

    for team in teams:
        if team["played"] > 0:
            if highest == []:
                highest.append(team)
            elif team["points"] > highest[0]["points"]:
                highest.clear()
                highest.append(team)
            elif team["points"] == highest[0]["points"]:
                highest.append(team)
    
    if highest == []:
        print("")
        logging.warning("No teams were played.\n")
        return

    print("Best attacking teams: ")
    for team in highest:
        print(team["name"])
    
    print("")
    logging.info("Best rating teams were printed.\n")
    return

def success_rate():
    for team in teams:
        if team["played"] == 0 or team["points"] == 0:
             print(f"{team["name"]}: No Games.")
        else:
            print(f"{team["name"]}: {(team["points"] / (team["played"] * 3)) * 100:.2f}%")

    print("")
    logging.info("Teams success rate were printed.\n")
    return

def winless_teams():
    for team in teams:
        if team["played"] > 0 and team["wins"] == 0:
            print(f"{team["name"]}: Games - {team["played"]}, Points - {team["points"]}")
        
    print("")
    logging.info("Winless teams were printed.\n")
    return

def tournament_summary():
    print("")
    logging.info("Tournament Summary\n")
    print(f"Teams: {len(teams)}\nGames: {len(matches)}")
    
    total_goals = 0
    for team in teams:
        total_goals += team["points"]
    print(f"Total goals: {total_goals}")

    total_goals = 0
    draw_games = 0
    for match in matches:
        total_goals += match["home_goals"]
        total_goals += match["away_goals"]
        if match["home_goals"] == match["away_goals"]:
            draw_games += 1

    print(f"Average goals per game: {total_goals / len(matches)}")
    print(f"Number of draw games: {draw_games}")
    print(f"1st team: {ranking_table()[0]["name"]}")
