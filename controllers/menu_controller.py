import sys
from tinydb import TinyDB
from controllers import database_controller
from controllers import players_controller, tournament_controller
from controllers.create_menu import CreateMenu
from views.display_menu import ShowMain, ShowPlayers
from views.display_menu import ViewDisplay


class MainMenuController:
    """Displays the main menu titles and links to sub-menus"""

    def __init__(self):
        self.view = ShowMain()
        self.menu_create = CreateMenu()
        self.controller_choice = None
        self.selected_players = ShowPlayers()

    def __call__(self):
        self.view.show_menu_detail()
        entry = self.menu_create(self.menu_create.main_menu)
        if entry == "1":
            self.controller_choice = PlayerMenuController()
            self.player_menu_controller_choice()
        if entry == "2":
            self.controller_choice = TournamentMenuController()
            self.tournament_menu_controller_choice()
        if entry == "3":
            self.controller_choice = AppControllerExit()
            self.exit_app_controller_choice()

    def player_menu_controller_choice(self):
        return self.controller_choice()

    def tournament_menu_controller_choice(self):
        return self.controller_choice()

    def exit_app_controller_choice(self):
        return self.controller_choice()


class PlayerMenuController(MainMenuController):
    def __init__(self):
        super().__init__()
        self.db = TinyDB("data_base.json")
        self.serialized_player_table = self.db.table("Player")
        # self.player_table = self.db.table('Player')
        self.all_player = self.serialized_player_table.all()
        self.create_player = players_controller.PlayerController()
        # self.players_score_ranking = players_controller.PlayerController()
        self.players_report = players_controller.PlayerReport()
        self.main_menu_controller = MainMenuController()
        # self.menu_load_player_controller = pc.LoadPlayer.show_in_menu()

    def __call__(self):
        entry = self.menu_create(self.menu_create.player_menu)
        # while True:
        if entry == "1":
            self.controller_choice = (
                database_controller.DatabaseWorker.save_player_in_db(
                    self.create_player.create_player(), self.db
                )
            )
            self.controller_choice = self.main_menu_controller()
        if entry == "2":
            self.create_player.update_player_score_rank(
                self.all_player, self.serialized_player_table
            )
            self.controller_choice = self.main_menu_controller()
        if entry == "3":
            self.controller_choice = self.players_report(self.db)
        if entry == "4":
            self.controller_choice = self.main_menu_controller()
        # else:
        # break


class TournamentMenuController(MainMenuController):
    def __init__(self):
        super().__init__()
        self.db = TinyDB("data_base.json")
        self.tdb = TinyDB("tournament_db.json")
        self.serialized_tournament_table = self.tdb.table("Tournament")
        self.serialized_player_table = self.db.table("Player")
        self.dict_tournament = self.serialized_tournament_table.all()
        self.all_player = self.serialized_player_table.all()
        self.tournament_report_controller = tournament_controller.TournamentReport()
        self.create_tournament = tournament_controller.TournamentController()
        self.run_tournament = tournament_controller.TournamentController()
        self.main_menu_controller = MainMenuController()

    def __call__(self):
        entry = self.menu_create(self.menu_create.tournament_menu)
        if entry == "1":
            self.controller_choice = self.create_tournament.create_tournament(
                self.db, self.tdb
            )
            self.controller_choice = self.main_menu_controller()
        if entry == "2":
            self.name__ = input("Enter The Name Of Tournament You Want To Search: ")
            self.controller_choice = self.run_tournament.run_tournament(
                self.name__, self.tdb, self.db
            )
            self.controller_choice = self.main_menu_controller()
        if entry == "3":
            self.controller_choice = self.run_tournament.resume_tournament(
                self.tdb, self.db
            )
            self.controller_choice = self.main_menu_controller()
        if entry == "4":
            name__ = input("Enter The Name Of Tournament You Want To Search: ")
            self.list_match = self.run_tournament.get_match_tournament(name__, self.tdb)
            ViewDisplay.display(self.list_match)
        if entry == "5":
            self.controller_choice = self.tournament_report_controller()
        if entry == "6":
            self.controller_choice = self.create_tournament.remove_tournament(self.db)
        if entry == "7":
            self.controller_choice = self.main_menu_controller()


class AppControllerExit:
    def __call__(self):
        sys.exit()
