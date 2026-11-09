from mock_data import *

def id_existed(team_id):
    for team in teams:
        if team["id"] == team_id:
            return True
    return False

def name_existed(name):
    for team in teams:
        if name == team["name"]:
            return True
    return False