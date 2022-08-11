import prettytable
from models import players
from models import tournament
from controllers import database_controller
from tinydb import TinyDB, Query, where
from views.display_board import *
from controllers.database_controller import *
from prettytable import PrettyTable
import views.tournament as t
from tabulate import tabulate



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



    def show_players_in_database(all_players): # all_players

        print(" ")
        print('========list player in data base...=======')
        print(" ")
        """for i, pl in enumerate(all_players):
            if i >= 0: i += 1
            x = PrettyTable()
            x.field_names = ["Index", "Last name", "First name", "Rank"]
            x.add_row([i, pl['Last name'], pl['First name'], pl['Rank']])
            print(x)"""
        for i, player in enumerate(all_players):
            print(f"\n-- Player no {i+1} --\n ")
            for k, v in player.items():
                if k in ["Index", "Last name", "First name", "Rank"]:
                    print(k+ " : "+ str(v))
                    print(" ")    
            

class DisplayPlayersReport:

    def __call__(self):
        print("----------------------------------\n"
              "        Display Players           \n"
              "----------------------------------\n"
             # " Display Reports :\n"
              )

    def display_player_scores(self, player_table):
        print(" ")
        print(" Players Ranking By Score")
        for i, player in enumerate( player_table):
            print(f"\n-- Player no {i+1} --\n ")
            for k, v in player.items():
                if k in ["Last name", "First name", "Rank", "Score"]:
                    print(k+ " : "+ str(v))
                    #print(" ")
                
            


    def display_alphabetical(self, all_players): # all_players
        print(" ")
        print("Players In Alphabetical Order")
        for i, pl in enumerate(all_players):
            print(f"\n-- Player no {i+1} --\n ")
            #if i >= 0: i += 1
            for k, v in pl.items():
                if k in ["Last name", "First name", "Date of birth", "Gender", "Rank"]:
                    print(k+ " : "+ str(v))
                    # print(" ")
             
            """table = [[pl]]
            print(tabulate(table))"""
            #print(f"\n -------------------- ")
           
      
        print("Press a letter to go back to rapport menu")
        input()

    def display_ranking(self, all_players):
        print(" ")
        print("Players In Rank Order")
        """for pl in all_players:
            x = PrettyTable()
            x.field_names = ["Rank", "Last name", "First name", "Date of birth", "Gender"]
            x.add_row(pl)
            print(x)"""
        for i, pl in enumerate(all_players):
            print(f"\n-- Player no {i+1} --\n ")
            for k, v in pl.items():
                if k in ["Rank", "Last name", "First name", "Date of birth", "Gender"]:
                    print(k+ " : "+ str(v))
            #print(f"\n -------------------- ")
            print(" ")


class DisplayTournamentsReport:

    def __call__(tournament_dict): # tournament_dict #all_tournament
        print("------------------------------------------------\n"
              "               Tournament Report                \n"
              "------------------------------------------------\n"
              " Display Reports :\n"
              ) 
        t.get_all_tournament(tournament_dict) # tournament_dict #all_tournament"""

        myTable = PrettyTable(["Tournament name", "Venue",  "Date", "Time-Control", "Number of players", "Number of Rounds"])
        myTable.add_row(tournament_dict)
        print(myTable)
        print('==========================================================')

            
    ##
    """def display_all_tournament_info(self, all_tournament_disp_info):
        myTable = PrettyTable(["Tournament ID", "Tournament name", "Venue",  "Date"])
        myTable.add_row(all_tournament_disp_info)
        print(myTable)"""
        ##

    def display_tournament_sel(self, tournament_sel):
        myTable = PrettyTable(["Tournament ID", "Tournament name", "Venue",  "Date", "Time-Control", "Number of players", "Number of Rounds"])
        myTable.add_row(tournament_sel)
        print(myTable)

        """for tn in tournament_sel:
            x = PrettyTable()
            x.field_names = ["Tournament ID", "Tournament name", "Venue",  "Date", "Time-Control", "Number of players", "Number of Rounds"]
            x.add_row(tournament_sel)
            print(x)"""
            #print(tn)
            
       
       
        
    """for i, tournament in enumerate(tournament_dict,1):
            print('Tournament identifiant: ', i)
            print(tournament)
            print()
    
        input("Appuyez sur une touche pour revenir au menu principal")"""


    
class DisplayPlayersByTournament:
    def __call__(self, list_player):
        print("----------------------------------\n"
              "           Players                \n"
              "----------------------------------\n"
              #" Display Reports :\n"
              )
              #player
        for player  in list_player:
            #print('================= player ================')
            #print(player)
           # print()
            x = PrettyTable()
            x.field_names = ["Last name", "First name",  "Rank"]
            x.add_row(player)
            print(x)

        
            
        #input("Appuyez sur une touche pour revenir au menu principal")

    

   
    
           




            