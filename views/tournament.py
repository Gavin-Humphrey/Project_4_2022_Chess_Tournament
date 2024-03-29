# import json
# from datetime import datetime
# from models.tournament import *


class TournamentView:
    """Display the list of all tournaments"""

    def get_all_tournament(tournament_list):
        print(" ")
        print("===== TOURNAMENT ====")
        for i, tournament in enumerate(tournament_list, 1):
            print("\n ---- Tournament ----\n")
            print("Tournament ID: ", i)
            for k, v in tournament.items():
                if k in [
                    "Tournament name",
                    "Venue",
                    "Date",
                    "Time-Control",
                    "Number of players",
                ]:
                    print(k + " : " + str(v))
            print("\n -------------------- ")

        print("======================")
