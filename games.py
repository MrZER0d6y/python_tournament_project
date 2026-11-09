from validations import *
from mock_data import teams, matches
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

def get_team_id(new_or_old):
    found_team_id = None
    while found_team_id != 0:
        try:
            team_id = int(input("Team ID: "))
        except ValueError:
            raise ValueError("integers only")
            continue

        if team_id < 0:
            logging.warning("Positive integers only.\n")
            continue
        
        if new_or_old == "new":
            if id_existed(team_id) == True:
                print("")
                logging.warning("Team ID is already existed, choose another one.\n")
                continue
            found_team_id = 0
        
        elif id_existed(team_id) == False:
            print("")
            logging.error("Team ID doesnt exists.\n")
            continue
        found_team_id = 0
    return team_id

def get_goals():
    while True:
        try:
            goals = int(input("Goals: "))
        except ValueError:
            raise ValueError("Integers only")
            continue
        
        if goals < 0:
            logging.warning("Positive integers only.\n")
            continue

        return goals

def get_name():
    while True:
        name = input("Name: ")
        if name_existed(name) == True:
            logging.warning(f"{name} name is already existed, choose another one.\n")
            continue

        if name == "":
            loggin.warning("Name must not be empty.\n")
            continue

        return name
        
def add_team():
    team_id = get_team_id("new")
    name = get_name()

    new_team = {"id": int(team_id), "name": name, "played": 0,
     "wins": 0, "draws": 0, "losses": 0,
     "goals_for": 0, "goals_against": 0, "points": 0}

    teams.append(new_team)
    logging.info("New team added (Team ID: %d, Name: %s).\n", team_id, name)

def show_teams():
    if teams == []:
        logging.warning("No teams found.\n")
        return

    for team in teams:
        print(f"\nTeam ID: {team["id"]}\nName: {team["name"]}\n"
        f"Games: {team["played"]}\nPoints: {team["points"]}")

    logging.info("All teams was printed.\n")
    return


def add_match_result():
    while True:
        home_team_id = get_team_id("old")
        away_team_id = get_team_id("old")

        home_exists = False
        away_exists = False

        if home_team_id == away_team_id:
            logging.warning("Teams are the same, choose different teams.\n")
            continue
        break

    for match in matches:
        if (match["home_team_id"] == home_team_id and match["away_team_id"] == away_team_id) or (match["home_team_id"] == away_team_id and match["away_team_id"] == home_team_id):
            logging.error("Teams already played together!\n")
            return

    home_goals = get_goals()
    away_goals = get_goals()
    
    match = {"home_team_id": home_team_id, "away_team_id": away_team_id, "home_goals": home_goals, "away_goals": away_goals}
    matches.append(match)
    print("")
    logging.info("Match added.\n")

    point_calculation(home_team_id, away_team_id, home_goals, away_goals)
    return

def point_calculation(home_team_id, away_team_id, home_goals, away_goals):
    for team in teams:
        if team["id"] == home_team_id:
            team["played"] += 1

            if home_goals > away_goals:
                print("")
                logging.info("Home won! (Team ID %d).\n", home_team_id)
                team["wins"] += 1
                team["points"] += 3
            elif home_goals < away_goals:
                print("")
                logging.info("Away won! (Team ID %d).\n", away_team_id)
                team["losses"] += 1
            else:
                print("")
                logging.info("Draw!\n")
                team["draws"] += 1
                team["points"] += 1
            
            team["goals_for"] += home_goals
            team["goals_against"] += away_goals

        elif team["id"] == away_team_id:
            team["played"] += 1

            if away_goals > home_goals:
                team["wins"] += 1
                team["points"] += 3
            elif away_goals < home_goals:
                team["losses"] += 1
            else:
                team["draws"] += 1
                team["points"] += 1
            
            team["goals_for"] += away_goals
            team["goals_against"] += home_goals

def ranking_table():
    return sorted(
        teams, 
        key=lambda team: (
            -team["points"], 
            -(team["goals_for"] - team["goals_against"]), 
            -team["goals_for"], 
            team["name"]
        )
    )

def check_championship_potential():
    num_teams = len(teams) - 1
    highest_potential = []
    points = 0

    for team in teams:
        remaining_games = num_teams - team["played"]
        max_points = team["points"] + remaining_games * 3

        if max_points >= points:
            highest_potential.clear()
            highest_potential.append(team["name"])
            points = max_points
    
    print("")
    logging.info("Championship Potential: \n")
    for team in highest_potential:
        print(f"{team}, points: {points}")