from models import players
from models import tournament
from controllers import database_controller
from tinydb import TinyDB, Query, where
from views.display_board import *
from controllers.database_controller import *


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
     
    def __call__(self):
        db = TinyDB('data_base.json')
        players_database = players.db   
        for p in players_database:
            print({'Last name':p.last_name, 'First name':p.first_name, 'Rank':p.rank})
