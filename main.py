from games import *
from validations import *
from mock_data import *
from logic import *
import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")

def main():
    choice = None
    while choice is not "0":
        print("========== TOURNAMENT MANAGER ==========\n")
        print("1. Add team\n2. Show all teams\n3. Add match result\n"
        "4. Show standings\n5. Show leading team\n6. Show best attacking team\n"
        "7. Show team success rate\n8. Show teams without wins\n9. Show tournament summary\n"
        "10. Check championship potential\n0. Exit\n")
        choice = input("Choose an option: ")

        if choice == "1":
            add_team()
        elif choice == "2":
            show_teams()
        elif choice == "3":
            add_match_result()
        elif choice == "4":
            table = ranking_table()
            for rank, team in enumerate(table, 1):
                gd = team["goals_for"] - team["goals_against"]
                print(f"{rank}. {team["name"]} | Games: {team["played"]} | Wins: {team["wins"]} "
                f"| Draws: {team["draws"]} | Losses: {team["losses"]} | Goals for: "
                f"{team["goals_for"]} | Goals against: {team["goals_against"]} "
                f"| GD: {gd:+} | Pts: {team["points"]}")

            logging.info("Ranking table printed\n")
        elif choice == "5":
            leading_team()
        elif choice == "6":
            best_attacking_team()
        elif choice == "7":
            success_rate()
        elif choice == "8":
            winless_teams()
        elif choice == "9":
            tournament_summary()
        elif choice == "10":
            check_championship_potential()
        elif choice == "0":
            logging.info("Exiting...")
            continue
        else:
            logging.error("Option not valid.")
        
    return 0

if __name__ == "__main__":
    main()