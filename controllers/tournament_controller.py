# from cmath import e
from datetime import datetime, date
import time

# from turtle import update
from tinydb import TinyDB, Query
import random
from models.tournament import *  # Tournament
from models import tournament
from models.players import Player
from controllers.database_controller import DatabaseWorker
import controllers.round_controller as RC
import controllers.match_controller as MC
import controllers.players_controller as PC
import controllers.database_controller as dc
from prettytable import PrettyTable
from models.round import Round
from views.display_menu import *  # ShowPlayers
from controllers import menu_controller
from controllers import create_menu
from views import display_menu
import views.tournament as tv
import views.tournament as t
from itertools import permutations


class TournamentController:
    @classmethod
    def create_tournament(cls, db, tdb):

        input_name = input("Please Enter Tournament Name: ")
        input_place = input("Please Enter Venue: ")
        stop = False
        while not stop:
            try:
                start_date = datetime.strptime(
                    input("Please Enter Tournament Start Date In (DD/MM/YYYY): "),
                    "%d/%m/%Y",
                ).strftime("%d/%m/%Y")
                stop = True
            except:
                print("Please Enter Tournament's Start Date In Format (DD/MM/YYYY")

        def nb_rounds():
            nb_rounds = 4
            print("The Number Of Rounds Is 4 By Default")
            valid_number = False
            while not valid_number:
                print("Enter 'Y' To Change, And 'N' To Continuer")
                choice = input(": ")
                if choice == "Y":
                    nb_rounds = input("Enter Number Of Rounds :")
                    if nb_rounds.isdigit():
                        valid_number = True
                    else:
                        print("Enter Digits")
                if choice == "N":
                    valid_number = True
            return nb_rounds

        def add_time_control():
            print("Please Choose Time-Control: ")
            time_control = None
            entry = input("Enter 1 For Bullet; 2 For Blitz; Or 3 For Rapid: ")
            if entry == "1":
                time_control = "Bullet"
            if entry == "2":
                time_control = "Blitz"
            if entry == "3":
                time_control = "Rapid"
            return time_control

        desc = input("Please Add Tournament Description Here: ")
        input_nb_player = input(
            "Please Enter The Number Of Players In This Tournament: "
        )
        serialized_player_table = db.table("Player")
        all_players = serialized_player_table.all()
        show_players_list = display_menu.ShowPlayers.show_players_in_database(
            all_players
        )
        indices = []
        choice_ = input("Please Enter Your Choice: ")
        if choice_ == "1":
            for i in range(int(input_nb_player)):
                indices.append(input(f"Please Enter The Index Of {i+1} Player  :"))
        else:
            indices = [
                random.randint(0, len(all_players)) for e in range(int(input_nb_player))
            ]

        list_players_ = [all_players[int(e) - 1] for e in indices]
        list_players = []
        for p in list_players_:
            p["Score"] = 0
            list_players.append(p)

        if list_players != []:
            list_indice = list(range(int(len(list_players) / 2)))
            list_players_ranking = cls.player_classment(list_players)
            list_pair = cls.player_pair(list_players_ranking, list_indice)
            list_match = cls.create_matchs(list_pair)
            round1 = RC.RoundController.create_round(list_match)
            tournament_ = tournament.Tournament(
                input_name,
                input_place,
                start_date,
                add_time_control(),
                nb_rounds(),
                [round1],
                input_nb_player,
                list_players,
                desc_=desc,
            )

            dc.DatabaseWorker.save_tournament_in_db(tournament_, tdb)
            return tournament_

    @classmethod
    def create_matchs(cls, list_pair):
        list_match = []
        for name_p1, name_p2 in list_pair:
            list_match.append(MC.MatchController.create_match(name_p1, name_p2))
        return list_match

    # What is this function for? #########
    @classmethod
    def get_player_name(cls, nb_player, db):  ###
        list_player = []
        for i in range(nb_player):
            print(f"Player {i+1} ")
            first_name = input("Please Enter Player's First Name: ")
            last_name = input("Please Enter Players Last Name: ")
            p, pfound = DatabaseWorker.get_player_by_name(last_name, first_name, db)
            if not pfound:
                print(
                    f"{last_name} {first_name} Does Not Exist. Please Register And Try Again"
                )
                return []
            else:

                list_player.append(p)
        return list_player

    @classmethod
    def order(cls, ditc_player):
        return ditc_player["Rank"]

    @classmethod
    def player_classment(cls, list_player):
        if len(list_player) % 2 != 0:
            return "To Start A Tournament, The Number Of Players Has To Be Pair"
        else:
            return [
                e["Last name"] + " " + e["First name"]
                for e in sorted(list_player, key=cls.order, reverse=True)
            ]

    @classmethod
    def player_pair(cls, list_player_ranking, indice_conf):
        if isinstance(list_player_ranking, list):
            return list(
                zip(
                    [
                        list_player_ranking[: int(len(list_player_ranking) / 2)][i]
                        for i in indice_conf
                    ],
                    list_player_ranking[int(len(list_player_ranking) / 2) :],
                )
            )

    @classmethod
    def get_tournament_by_name(cls, tournament_name, db):
        tournament_table = db.table("Tournament")
        tournament = Query()
        result = tournament_table.search(
            tournament["Tournament name"] == tournament_name
        )
        if result:
            return result[0]
        else:
            return

    @classmethod
    def is_tournament_finished(cls, tourn):
        if tourn:
            matchs = tourn["Rounds"][-1]["Match"]
            list_match = [match for match in matchs if isinstance(match["Score"], int)]
            return tourn["Number of Rounds"] == len(tourn["Rounds"]) and not list_match

    @classmethod
    def get_match_tournament(cls, tournament_name, db):
        menu_create = create_menu.CreateMenu()
        list_match = []
        tourn = cls.get_tournament_by_name(tournament_name, db)
        status = menu_create(menu_create.sub_tournaments_menu)

        if tourn:
            matchs = [m for r in tourn["Rounds"] for m in r["Match"]]

            # List match terminé
            if status == "1":
                list_match = [
                    match for match in matchs if isinstance(match["Score"], list)
                ]

                # Match non terminé
            elif status == "2":
                list_match = [
                    match for match in matchs if isinstance(match["Score"], int)
                ]
                # Tout les match

            elif status == "3":
                # all match list: ")
                list_match = matchs
            return list_match

    @classmethod
    def get_data(cls, tournament_name, db, pdb):
        t_dict = cls.get_tournament_by_name(tournament_name, db)
        tournament_table = db.table("Tournament")
        player_table = pdb.table("Player")
        return t_dict, tournament_table, player_table

    @classmethod
    def update_score_all_player(
        cls,
        list_player,
        last_name_p1,
        first_name_p1,
        last_name_p2,
        first_name_p2,
        score_p1,
        score_p2,
        m,
    ):
        for p in list_player:

            if p["Last name"] == last_name_p1 and p["First name"] == first_name_p1:
                p["Score"] = p["Score"] + score_p1
            elif p["Last name"] == last_name_p2 and p["First name"] == first_name_p2:
                p["Score"] = p["Score"] + score_p2
        m["Score"] = tuple([score_p1, score_p2])
        return m

    @classmethod
    def play_last_round_match(
        cls, t_dict, tournament_table, tournament_name, tour_query
    ):
        if t_dict:
            list_player = t_dict["Players"]
            matchs = t_dict["Rounds"][-1]["Match"]
            r = t_dict["Rounds"]
            all_match_terminated = True
            for i, m in enumerate(matchs):
                if isinstance(m["Score"], int):
                    random_float = random.uniform(0, 1)
                    if random_float >= 0.5:
                        col1, col2 = "Black", "White"
                    else:
                        col2, col1 = "Black", "White"

                    response_ = input(
                        f"If The Match Between {m['Player 1']} And {m['Player 2']} Is Terminated, Press 'y' "
                    )
                    if response_.lower() == "y":
                        score_p1 = float(
                            input(
                                f"Enter The Score Of {m['Player 1']}: Who Played In {col1} Color: "
                            )
                        )
                        score_p2 = float(
                            input(
                                f"Enter The Score Of {m['Player 2']}: Who Played In {col2} Color: "
                            )
                        )
                        name_p1 = m["Player 1"].split(" ")
                        last_name_p1, first_name_p1 = (
                            " ".join(name_p1[0:-1]),
                            name_p1[-1],
                        )
                        name_p2 = m["Player 2"].split(" ")
                        last_name_p2, first_name_p2 = (
                            " ".join(name_p2[0:-1]),
                            name_p2[-1],
                        )
                        list_score_enable = [(1, 0), (0, 1), (0.5, 0.5)]
                        stop = False
                        while not stop:
                            if (score_p1, score_p2) not in list_score_enable:
                                print("Enter 0, 0.5, or 1")
                                score_p1 = float(
                                    input(
                                        f"Enter The Score Of {m['Player 1']}: Who Played In {col1} Color: "
                                    )
                                )
                                score_p2 = float(
                                    input(
                                        f"Enter The Score Of {m['Player 2']}: Who Played In {col2} Color: "
                                    )
                                )
                            else:
                                stop = True

                        dif = score_p1 - score_p2
                        if dif in [-2, 1]:
                            print(
                                f"{last_name_p1} {first_name_p1} Will Win This Match!"
                            )
                        elif dif in [-1, 2]:
                            print(
                                f"{last_name_p2} {first_name_p2} Will Win This Match!"
                            )
                        else:
                            print("This Match Will End In A Draw!")
                        print("")
                        r[-1]["Match"][i] = cls.update_score_all_player(
                            list_player,
                            last_name_p1,
                            first_name_p1,
                            last_name_p2,
                            first_name_p2,
                            score_p1,
                            score_p2,
                            m,
                        )
                        tournament_table.update(
                            {"Rounds": [r]},
                            tour_query["Tournament name"] == tournament_name,
                        )
                        tournament_table.update(
                            {"Players": list_player},
                            tour_query["Tournament name"] == tournament_name,
                        )
                    else:
                        all_match_terminated = False
        return all_match_terminated, r

    @classmethod
    def update_create_round(
        cls,
        t_dict,
        r,
        tournament_name,
        db,
        tournament_table,
        player_table,
        tournament,
        player,
    ):
        r[-1]["End date"] = datetime.now().strftime("%d/%m/%Y %H:%M")
        tournament_table.update(
            {"Rounds": r}, tournament["Tournament name"] == tournament_name
        )

        update_score = input("Round Matches Terminated.Press 'y' To Update Score: ")
        if update_score.lower() == "y":
            matchs = r[-1]["Match"]
            score_by_name = {}
            for ma in matchs:
                score_by_name[" ".join(ma["Player 1"].split(" ")[0:-1])] = ma["Score"][
                    0
                ]
                score_by_name[" ".join(ma["Player 2"].split(" ")[0:-1])] = ma["Score"][
                    1
                ]

            for k, v in score_by_name.items():
                score = v
                s = player_table.search(player["Last name"] == k)
                if s:
                    score += s[0]["Score"]
                else:
                    print(k, "Does Not Exist")

                player_table.update({"Score": score}, player["Last name"] == k)
            print(matchs)

        if t_dict["Number of Rounds"] > len(r):
            new_r = input(" Do You Want To Start A New Round?  If Yes, Press 'Y': ")
            if new_r.lower() == "y":
                cls.add_round(t_dict, tournament_table, tournament, tournament_name)
        else:
            print(" ")
            print("This Tournament Is Ended")

    @classmethod
    def run_tournament(cls, tournament_name, db, pdb):

        t_dict, tournament_table, player_table = cls.get_data(tournament_name, db, pdb)
        tournament = Query()
        player = Query()

        all_match_terminated, r = cls.play_last_round_match(
            t_dict, tournament_table, tournament_name, tournament
        )
        if all_match_terminated:
            cls.update_create_round(
                t_dict,
                r,
                tournament_name,
                db,
                tournament_table,
                player_table,
                tournament,
                player,
            )

        else:
            print("The Tournament You Are Looking For Does Not Exist In Our Database")

    @classmethod
    def resume_tournament(cls, db, pdb):
        tournament_table = db.table("Tournament")
        all_tournament = tournament_table.all()
        not_finished_tournament = [
            t for t in all_tournament if not cls.is_tournament_finished(t)
        ]
        tv.get_all_tournament(not_finished_tournament)

        enter_index = False
        while not enter_index:
            try:
                tournament_index = input("Please Enter The Index Of Tournqment : ")
                tourn_to_resume = not_finished_tournament[int(tournament_index) - 1][
                    "Tournament name"
                ]
                cls.run_tournament(tourn_to_resume, db, pdb)
                enter_index = True
            except:
                print("Please Enter A Valid Tournament Index")

    @classmethod
    def add_round(
        cls, tournament, tournament_table, tournament_query, tournament_name_
    ):
        round_ = tournament["Rounds"]
        matchs = round_[-1]["Match"]
        nb_player = int(tournament["Number of players"])
        is_round_ended = True
        for match in matchs:
            if isinstance(match["Score"], int):
                is_round_ended = False
                break
        if is_round_ended and len(round_) < tournament["Number of Rounds"]:
            print("Enter 'Y' To Start A New Round")
            choice = input(": ")
            if choice.lower() == "y":
                name_round = input("Please Enter The New Round Name: ")
                round_date_begin = datetime.now().strftime("%d/%m/%Y %H:%M")
                list_tournament_player = tournament["Players"]
                sort_one_level = sorted(
                    list_tournament_player,
                    key=lambda x: (x["Score"], x["Rank"]),
                    reverse=True,
                )

                list_finale = [
                    e["Last name"] + " " + e["First name"]
                    for e in cls.ordre_level_three(sort_one_level)
                ]

                print(" ")
                print(" ")

                list_match_in_round = [r["Match"] for r in round_]
                list_match_old_round = []
                for l in list_match_in_round:
                    for w in l:
                        list_match_old_round.append((w["Player 1"], w["Player 2"]))
                print(" ")

                all_config = list(
                    permutations(list(range(int(nb_player / 2))), int(nb_player / 2))
                )
                stop = False
                indice_conf = 0

                while indice_conf < len(all_config) and not stop:
                    list_pair = cls.player_pair(list_finale, all_config[indice_conf])
                    if all(
                        [
                            (z, w) not in list_match_old_round
                            and (w, z) not in list_match_old_round
                            for (z, w) in list_pair
                        ]
                    ):
                        stop = True
                    indice_conf += 1
                if indice_conf > len(all_config):
                    print("Match List Is Empty. You Cannot Create A New Round")
                else:
                    list_match = cls.create_matchs(list_pair)
                    new_round = Round(name_round, list_match)
                    round_.append(
                        {
                            "Round name": new_round.round_name,
                            "Start date": round_date_begin,
                            "Match": [
                                {
                                    "Player 1": m.player1,
                                    "Player 2": m.player2,
                                    "Score": m.score,
                                }
                                for m in list_match
                            ],
                        }
                    )
                    tournament_table.update(
                        {"Rounds": round_},
                        tournament_query["Tournament name"] == tournament_name_,
                    )

                    print(" ")
                    print(" ")

            elif len(round_) == tournament["Number of Rounds"]:
                print("You Cannot Create A New Round. Number Of Rounds Attained!")

            else:
                print("Cannot Start A New Round. Previous Round Not Terminated")

    @classmethod
    def ordre_level_three(cls, list_player):
        stop = False
        while not stop:
            stop = True
            for i in range(len(list_player) - 1):
                if (list_player[i + 1]["Score"] == list_player[i]["Score"]) and (
                    list_player[i + 1]["Rank"] == list_player[i]["Rank"]
                ):
                    if list_player[i + 1]["Last name"] < list_player[i]["Last name"]:
                        item_indice_i = list_player[i]
                        list_player[i] = list_player[i + 1]
                        list_player[i + 1] = item_indice_i
                        stop = False
        return list_player

    @classmethod
    def remove_tournament(cls, db):
        tournament_table = db.table("Tournament")
        tournament = Query()
        tournament_name = input("Enter The Tournament Name You Want To Delete:  ")
        confirmation = input(
            f"Are You Sure You Want To Delete {tournament_name}? If Yes Press 'y': "
        )
        if confirmation.lower() == "y":
            tournament_table.remove(tournament["Tournament name"] == tournament_name)


class TournamentReport:
    def __call__(self):  # , dict_tournament, list_player, db, tdb
        db = TinyDB("data_base.json")
        Player = Query()
        Table_player = db.table("Player")
        tdb = TinyDB("tournament_db.json")
        self.menu_create = create_menu.CreateMenu()
        self.main_menu_controller = menu_controller.MainMenuController()
        self.display_player = display_menu.DisplayPlayersReport()
        self.display_tournament = display_menu.DisplayTournamentsReport()
        self.display_player_by_tournament = display_menu.DisplayPlayersByTournament()
        self.display_all_tournaments = t
        serialized_player_table = db.table("Player")
        self.players_db = serialized_player_table.all()
        serialized_tournament_table = tdb.table("Tournament")
        self.all_tournament = serialized_tournament_table.all()

        # Display all the tournaments
        # self.display_tournament(self.all_tournament)
        # self.display_tournament(self.dict_tournament)
        entry = self.menu_create(self.menu_create.tournaments_report_menu)
        if entry == "1":
            # self.display_tournament(self.all_tournament)
            ##
            # tournament_display_info = self.display_tournament(tour_info_to_disp)# self.all_tournament
            self.info_to_disp = self.all_tournament
            self.display_all_tournaments.get_all_tournament(self.all_tournament)

            ##
            # self.display_tournament = self.main_menu_controller(self.all_tournament, self.players_db, db, tdb)  #self.all_tournament, self.players_db, db, tdb
            # input("Enter a letter to return to Main Menu")
            TournamentReport.__call__(self)
            # Choose a tournament
        if entry == "2":
            valid_choice = True
            while valid_choice:
                identifiant_tournament = input(
                    "Enter The Tournament ID You Want To Display: "
                )
                choice_tournament = self.all_tournament[int(identifiant_tournament) - 1]
                tournament_sel = [
                    identifiant_tournament,
                    choice_tournament["Tournament name"],
                    choice_tournament["Venue"],
                    choice_tournament["Date"],
                    choice_tournament["Time-Control"],
                    choice_tournament["Number of players"],
                    choice_tournament["Number of Rounds"],
                ]
                print(" ")
                print("TOURNAMENT")
                print(" ")
                self.display_tournament.display_tournament_sel(tournament_sel)

                choice_tournament = self.all_tournament[int(identifiant_tournament) - 1]
                list_player_ = [
                    {
                        "Last name": w["Last name"],
                        "First name": w["First name"],
                        "Rank": w["Rank"],
                    }
                    for w in choice_tournament["Players"]
                ]  # [(p['Last name'], p['First name'], p['Rank'])
                # for p in choice_tournament['Players']]
                self.display_player_by_tournament(
                    sorted(list_player_, key=lambda x: x["Last name"])
                )

                print(" ")
                print("ROUND")
                print(" ")
                print(choice_tournament["Rounds"])
                l_round_choice = [
                    (r["Round name"], r["Start date"])
                    for r in choice_tournament["Rounds"]
                ]
                print(l_round_choice)
                print(" ")
                print("MATCH")
                print(" ")
                print([r["Match"] for r in choice_tournament["Rounds"]])
                print(" ")
                valid_choice = False
                TournamentReport.__call__(self)
                self.main_menu_controller(self)

                """
                # To print the dictionary of the tournament
                #print(choice_tournament)
                entry = self.menu_create(self.menu_create.sub_tournaments_report_menu)
                # Display the players in the chosen Tournament in alphabetical order
                if entry == "1":
                    entry = self.menu_create(self.menu_create.players_report_menu)
                if entry == "1":
                    #identifiant_tournament = input("Enter Tournament  : ")
                    choice_tournament = self.all_tournament[int(identifiant_tournament)-1]
                    list_player_ = [(p['Last name'], p['First name'], p['Rank']) 
                    for p in choice_tournament['Players']]
                    self.display_player_by_tournament(sorted(list_player_, key = lambda x: x[0]))
                    input("Enter any letter to return to Main Menu: ")
                    #TournamentReport.__call__(self)
 
                    # Display the players in the chosen Tournament in ranking order
                    entry = self.menu_create(self.menu_create.players_report_menu)
                    if entry == "2":
                        choice_tournament = self.all_tournament[int(identifiant_tournament)-1]
                        self.display_player_by_tournament(sorted(list_player_, key = lambda x: x[2],reverse=True))
                        input("Enter any letter to return to Main Menu: ")   
                        #TournamentReport.__call__(self)
                       
                # Display the Rounds in the chosen Tournament
                entry = self.menu_create(self.menu_create.sub_tournaments_report_menu)
                if entry == "2":
                    print(choice_tournament['Rounds'])
                    l_round_choice = [(r['Round name'], r['Start date']) 
                    for r in choice_tournament['Rounds']]
                    print(l_round_choice)

                    input("Enter any letter to return to Main Menu: ")
                    TournamentReport.__call__(self)

                # Display the matches in chosen Tournament 
                entry = self.menu_create(self.menu_create.sub_tournaments_report_menu)
                if entry == "3":
                    print([r['Match'] for r in choice_tournament['Rounds']])
                    input("Enter any letter to return to Main Menu: ")
                    #TournamentReport.__call__(self)"""

                # Go to main menu
                if entry == "4":
                    valid_choice = False
                    TournamentReport.__call__(self)
                    self.main_menu_controller(self)

                """# Display all the tournaments
                #self.display_tournament()
                entry = self.menu_create(self.menu_create.tournaments_report_menu)
                if entry == "1":
                    self.display_tournaments = self.main_menu_controller(self.all_tournament, self.players_db, db, tdb)  #self.all_tournament, self.players_db, db, tdb
                    self.main_menu_controller()
                # Choose a tournament
                if entry == "2":
                    identifiant_tournament = input("Enter Tournament  : ")
                    choice_tournament = self.all_tournament[int(identifiant_tournament)-1]
                    print(choice_tournament)
                    TournamentReport.__call__(self)"""

        else:  # Go to main menu
            if entry == "3":
                valid_choice = False
                self.main_menu_controller()

            print("Enter The Number Corresponding To Your Choice")
