from prettytable import PrettyTable
import views.tournament as t


class ViewDisplay:
    @classmethod
    def display(cls, message: str):
        """Print a message"""
        print(message)


class ShowMain:
    """Show main menu display"""

    def show_menu_detail(self):

        print(
            "|---------|-------------------------------|--------|\n"
            "|         |     Tournament Management     |        |\n"
            "|---------|-------------------------------|--------|\n"
            "|---------|-------------------------------|--------|\n"
            "|         |          Main Menu            |        |\n"
            "|---------|-------------------------------|--------|\n"
            "|---------|-------------------------------|--------|\n"
            "|         | Enter a number of your choice |        |\n"
            "|---------|-------------------------------|--------|\n"
        )


class ShowTournament:
    def __call__(self):
        """tdb = TinyDB("tournament_db.json")
        not_started_tournament = False
        tournaments_db = tournament.tdb

        for t in tournaments_db:
            if t.rounds == []:
                print({"Name": t.name, "Venue": t.place})
                not_started_tournament = True

        return not_started_tournament"""


class ShowPlayers:
    """Displays all the actors in the database"""

    def show_players_in_database(all_players):
        print(" ")
        print("========list player in data base...=======")
        print(" ")
        for i, player in enumerate(all_players):
            print(f"\n-- Player no {i+1} --\n ")
            for k, v in player.items():
                if k in ["Index", "Last name", "First name", "Rank"]:
                    print(k + " : " + str(v))
                    print(" ")


class DisplayPlayersReport:
    """Displays all the players in Score ranking, Ranks, and Alphabetical order"""

    def __call__(self):
        print(
            "----------------------------------\n"
            "        Display Players           \n"
            "----------------------------------\n"
        )

    def display_player_scores(self, player_table):
        print(" ")
        print(" Players Ranking By Score")
        for i, player in enumerate(player_table):
            print(f"\n-- Player no {i+1} --\n ")
            for k, v in player.items():
                if k in ["Last name", "First name", "Rank", "Score"]:
                    print(k + " : " + str(v))

    def display_alphabetical(self, all_players):
        print(" ")
        print("Players In Alphabetical Order")
        for i, pl in enumerate(all_players):
            print(f"\n-- Player no {i+1} --\n ")
            for k, v in pl.items():
                if k in ["Last name", "First name", "Date of birth", "Gender", "Rank"]:
                    print(k + " : " + str(v))

        print("Press A Letter To Go Back To Report Menu")
        input()

    def display_ranking(self, all_players):
        print(" ")
        print("Players In Rank Order")
        for i, pl in enumerate(all_players):
            print(f"\n-- Player no {i+1} --\n ")
            for k, v in pl.items():
                if k in ["Rank", "Last name", "First name", "Date of birth", "Gender"]:
                    print(k + " : " + str(v))
            print(" ")


class DisplayTournamentsReport:
    """Displays all the tournaments, and a selected tournament in detail"""

    def __call__(tournament_dict):
        print(
            "------------------------------------------------\n"
            "               Tournament Report                \n"
            "------------------------------------------------\n"
            " Display Reports :\n"
        )
        t.TournamentView.get_all_tournament(tournament_dict)

        myTable = PrettyTable(
            [
                "Tournament name",
                "Venue",
                "Date",
                "Time-Control",
                "Number of players",
                "Number of Rounds",
            ]
        )
        myTable.add_row(tournament_dict)
        print(myTable)
        print("==========================================================")

    # To select and display a tournament
    def display_tournament_sel(self, tournament_sel):
        myTable = PrettyTable(
            [
                "Tournament ID",
                "Tournament name",
                "Venue",
                "Date",
                "Time-Control",
                "Number of players",
                "Number of Rounds",
            ]
        )
        myTable.add_row(tournament_sel)
        print(myTable)


class DisplayPlayersByTournament:
    """Displays the players in a selected tournament"""

    def __call__(self, list_player):
        print(" ")
        print("------------------\n" "      Players     \n" "------------------\n")

        for i, pl in enumerate(list_player):
            print(f"\n-- Player no {i+1} --\n ")
            for k, v in pl.items():
                if k in ["Last name", "First name", "Date of birth", "Gender", "Rank"]:
                    print(k + " : " + str(v))
