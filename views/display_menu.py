from models import players
from models import tournament
from controllers import database_controller
from tinydb import TinyDB, Query, where
from views.display_board import *
from controllers.database_controller import *
from prettytable import PrettyTable


class ShowMain:
    
    def show_menu_detail(self):
        
        print("|---------|-------------------------------|--------|\n"
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
        tdb = TinyDB('tournament_db.json')
        not_started_tournament = False
        tournaments_db = tournament.tdb

        for t in tournaments_db:
            if t.rounds == []:
                print({'Name':t.name, 'Venue':t.place})
                not_started_tournament = True

        return not_started_tournament


class ShowPlayers:
     
    """def __call__(self):
        db = TinyDB('data_base.json')
        players_database = players.db   
        for p in players_database:
            print({'Last name':p.last_name, 'First name':p.first_name, 'Rank':p.rank})"""



    def show_players_in_database(all_players):

        print(" ")
        print('========list player in data base...=======')
        print(" ")
        for i, pl in enumerate(all_players):
            if i >= 0: i += 1
            """print('===========================\n')
            print(f'information for player {i+1}\n')
            print('===========================\n')
            print(f"indice: {i} | Last name:  {pl['Last name']} | First name:  {pl['First name']}  | Rank:  {pl['Rank']}\n")"""
            x = PrettyTable()
            x.field_names = ["Index", "Last name", "First name", "Rank"]
            x.add_row([i, pl['Last name'], pl['First name'], pl['Rank']])
            print(x)

class DisplayPlayersReport:

    def __call__(self):
        print("------------------------------------------------\n"
              "                 Display Players                \n"
              "------------------------------------------------\n"
              " Display Reports :\n"
              )

    def display_alphabetical(self, all_players):
        print(" ")
        print("              Players In Alphabetical Order")
        for pl in all_players:
            #print(pl)
            x = PrettyTable()
            x.field_names = ["Last name", "First name", "Date of birth", "Gender", "Rank"]
            x.add_row(pl)
            print(x)
        print("Press a letter to go back to rapport menu")
        input()

    def display_ranking(self, all_players):
        print(" ")
        print("                  Players In Rank Order")
        for pl in all_players:
            x = PrettyTable()
            x.field_names = ["Rank", "Last name", "First name", "Date of birth", "Gender"]
            x.add_row(pl)
            print(x)


class DisplayTournamentsReport:

    def __call__(self):
        print("------------------------------------------------\n"
              "               Tournament Report                \n"
              "------------------------------------------------\n"
              " Display Reports :\n"
              )





           




            