from datetime import datetime
from tinydb import Query
from controllers import menu_controller
from controllers.create_menu import CreateMenu
from models.players import Player
from views import display_menu
from views.display_menu import ViewDisplay


class PlayerController:
    """
    Creates and adds players to database by entering player's details,
    then add update player's scores and ranks to the database
    """

    @classmethod
    def get_list_player(cls, nb_player):
        list_player = []
        for i in range(nb_player):
            stop_rank = False
            stop_dob = False
            last_name = input("Please enter player {} last name: ".format(i + 1))
            first_name = input("Please enter player {} first name: ".format(i + 1))
            while not stop_dob:
                try:
                    dob = datetime.strptime(
                        input(
                            "Please enter player {} date of birth in (DD/MM/YYYY): ".format(
                                i + 1
                            )
                        ),
                        "%d/%m/%Y",
                    ).strftime("%d/%m/%Y")
                    stop_dob = True
                except Exception:
                    ViewDisplay.display(
                        "Please enter player's date of birth in format (DD/MM/YYYY"
                    )
            gender = input("Please enter player {} gender: ".format(i + 1))
            while not stop_rank:
                try:
                    rank = int(input("Please enter player {} rank: ".format(i + 1)))
                    stop_rank = True
                except Exception:
                    ViewDisplay.display("Attributed rank should be a number")

            p = Player(last_name, first_name, dob, gender, rank)
            ViewDisplay.display(p)
            list_player.append(p)
        return list_player

    @classmethod
    def create_player(cls):
        stop = False
        while not stop:
            try:
                nb_player = int(
                    input("Please enter the number of players you want to create: ")
                )
                stop = True
            except Exception:
                ViewDisplay.display("Please enter a number ")
            else:
                return cls.get_list_player(nb_player)

    # Displays players ranking by scores
    @classmethod
    def display_player_scores(cls, player_table):
        ViewDisplay.display(" ")
        ViewDisplay.display("   Players Ranking By Score")
        for i, player in enumerate(player_table, 1):
            ViewDisplay.display(f"\n-- Player no {i} --\n")
            for k, v in player.items():
                if k in ["Last name", "First name", "Rank", "Score"]:
                    ViewDisplay.display(k + " : " + str(v))

    # Updates  players ranking
    @classmethod
    def update_player_score_rank(cls, all_players, player_table):
        cls.display_player_scores(all_players)
        player = Query()

        valid = False
        while not valid:
            choice = input(
                f"Please Enter Player ID Between 1 And {len(all_players)} That You Want To Update Score | Rank: "
            )
            try:
                if int(choice) <= len(all_players) or int(choice) >= 1:
                    last_name = all_players[int(choice) - 1]["Last name"]
                    valid = True
            except Exception:
                pass
        new_rank = int(input("Please Enter The New Rank : "))
        player_table.update({"Rank": new_rank}, player["Last name"] == last_name)
        """ViewDisplay.display(
            '1: Update Rank\n \n2: Update Score\n3: Update Score And Rank\n'
        )
        choice = input("Please Enter Your Choice: ")"""

        if choice == "1":
            new_rank = int(input("Please Enter The New Rank : "))
            player_table.update({"Rank": new_rank}, player["Last name"] == last_name)
        elif choice == "2":
            new_score = int(input("Please Enter The New Score : "))
            player_table.update({"Score": new_score}, player["Last name"] == last_name)
        elif choice == "3":
            new_score = int(input("Please Enter The New Score : "))
            new_rank = int(input("Please Enter The New Rank : "))
            player_table.update({"Score": new_score}, player["Last name"] == last_name)
            player_table.update({"Rank": new_rank}, player["Last name"] == last_name)

    @classmethod
    def display_all_players(cls, db):

        pass


class PlayerReport:
    """Displays all the actors, sorts and displays players by ranks, and by alphabets"""

    def __call__(self, db):
        self.menu_create = CreateMenu()
        self.main_menu_controller = menu_controller.MainMenuController()
        self.display_player = display_menu.DisplayPlayersReport()
        serialized_player_table = db.table("Player")
        self.players_db = serialized_player_table.all()
        self.players_score_ranking = PlayerController()
        self.player = Query()
        self.display_player()

        # Select to display all players, by rank, by alphabet, and by score
        entry = self.menu_create(self.menu_create.players_report_menu)
        while True:
            if entry == "1":
                self.player_score = self.players_score_ranking.display_all_players(
                    serialized_player_table
                )
                list_player_score = sorted(
                    serialized_player_table, key=lambda x: x["Score"], reverse=True
                )
                self.display_player.display_player_scores(list_player_score)
                PlayerReport.__call__(self, db)
            elif entry == "2":
                player_by_name = [
                    {
                        "Last name": w["Last name"],
                        "First name": w["First name"],
                        "Date of birth": w["Date of birth"],
                        "Gender": w["Gender"],
                        "Rank": w["Rank"],
                    }
                    for w in self.players_db
                ]
                player_by_name.sort(key=lambda x: x["Last name"])
                self.display_player.display_alphabetical(player_by_name)
                PlayerReport.__call__(self, db)
            elif entry == "3":
                player_by_rank = [
                    {
                        "Rank": w["Rank"],
                        "Last name": w["Last name"],
                        "First name": w["First name"],
                        "Date of birth": w["Date of birth"],
                        "Gender": w["Gender"],
                    }
                    for w in self.players_db
                ]
                player_by_rank.sort(key=lambda x: x["Rank"], reverse=True)
                self.display_player.display_ranking(player_by_rank)
                PlayerReport.__call__(self, db)
            elif entry == "4":
                self.main_menu_controller()
            else:
                return self.main_menu_controller()
