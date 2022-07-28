from datetime import datetime, date

from tinydb import TinyDB, Query
import random
from models.tournament import Tournament
from models import tournament
from models.players import Player
from controllers.database_controller import DatabaseWorker
import controllers.round_controller as RC
import controllers.match_controller as MC
import controllers.database_controller as dc
from models.round import Round
from views.display_menu import ShowPlayers
from controllers import menu_controller
from controllers import create_menu
from views import display_menu 




class TournamentController:
    @classmethod
    def create_tournament(cls, db,tdb):
        """name__ = input('entrer the name of tournament that we want to search: ')
        #result = cls.get_tournament_by_name(name__, tdb)
        print('name__',name__)
        cls.run_tournament(name__,tdb)"""
        
        input_name = input("Please enter name of the tournament: ")
        input_place = input("Please enter the venue: ")
        stop = False
        while not stop:
                    try:
                        start_date = datetime.strptime(input("Please enter tournament  date of satrt in (DD/MM/YYYY): "), "%d/%m/%Y").strftime("%d/%m/%Y")
                        stop = True
                    except:
                        print("Please enter tournament's start date in format (DD/MM/YYYY")
        input_nb_player = input("Please enter the number of players in the tournament: ")
        serialized_player_table =  db.table('Player')#
        all_players = serialized_player_table.all()#
        show_players_list = ShowPlayers.show_players_in_database(all_players)#
        """serialized_player_table =  db.table('Player')
        all_players = serialized_player_table.all()
        print('========list player in data base...=======')
        for i, pl in enumerate(all_players):
            print('===========================\n')
            print(f'information for player {i+1}\n')
            print('===========================\n')
            print(f"indice: {i} | Last name:  {pl['Last name']} | First name:  {pl['First name']}  | Rank:  {pl['Rank']}\n")"""
        indices = []
        choice_ = int(input('Please entrer your choice: '))
        if choice_ == 1:
            for i in range(int(input_nb_player)):
                indices.append(input(f'Please enter the index of {i+1} player  :'))
            print('indices', indices)
        else:
            indices = [ random.randint(0, len(all_players)) for e in range(int(input_nb_player))]
         
        list_players = [all_players[int(e)] for e in indices]

        #nb_rounds = input("Please enter the number of rounds for this tournament")
        
        def nb_rounds():   
            nb_rounds = 4
            print("The number of rounds is 4 by default\n"
                    "Do you want to change this number ?")
            valid_number = False
            while not valid_number:
                print("Enter 'Y' to change, and 'N' to continuer")
                choice = input(": ")
                if choice == "Y":
                    nb_rounds = input("Enter number of rounds :")
                    if nb_rounds.isdigit():
                        valid_number = True
                    else:
                        print("Enter digits")
                if choice == "N":
                    valid_number = True
            return nb_rounds
        
        def add_time_control():
            print("Please chose time-control: ")
            time_control = None
            entry = input("Enter 1 for Bullet; 2 for Blitz; or 3 for Rapid: ")
            if entry == "1":
                time_control = "Bullet"
            if entry == "2":
                time_control = "Blitz"
            if entry == "3":
                time_control = "Rapid"
            return time_control

        if list_players != []:
            print('list_player', list_players)
            list_players_ranking = cls.player_classment(list_players) 
            list_pair = cls.player_pair(list_players_ranking) 
            list_match = cls.create_matchs(list_pair)
            round1 = RC.RoundController.create_round(list_match)
            tournament_ = tournament.Tournament(input_name, input_place, start_date, add_time_control(),
                    input_nb_player, list_players, nb_rounds(), [round1])
            dc.DatabaseWorker.save_tournament_in_db(tournament_, tdb)
            return tournament_
       
    @classmethod
    def create_matchs(cls, list_pair):
        list_match = []
        for name_p1, name_p2 in list_pair:
            list_match.append(MC.MatchController.create_match(name_p1, name_p2))
        return list_match
     
    @classmethod
    def get_player_name(cls, nb_player, db):
        list_player = []
        for i in range(nb_player):
            print(f"Player {i+1} ")
            first_name = input("Please enter player's first name: ")
            last_name = input("Please enter players last name: ")
            p, pfound = DatabaseWorker.get_player_by_name(last_name, first_name, db)
            if not pfound:
                print(f"Player {last_name} {first_name} does not exist in the database. Please register this player and try again")
                # To do: add menu choice. 1st choice: reenter new player name; 2nd choice: go to the main menu to create a new player
                return []
            else:
                
                list_player.append(p)
        return list_player

    @classmethod   
    def order(cls, ditc_player):
        return ditc_player ['Rank']

    @classmethod
    def player_classment(cls, list_player):
        if len(list_player) % 2 != 0:
            return "We are sorry we can't start a tournament, the number of players has to be pair"
        else:
            return [ e ['Last name'] +' '+ e ['First name'] for e in sorted(list_player, key = cls.order, reverse=True)]
        
    @classmethod
    def player_pair(cls, list_player_ranking):
        if isinstance(list_player_ranking, list):
            return list(zip(list_player_ranking[:int(len(list_player_ranking)/2)], list_player_ranking[int(len(list_player_ranking)/2):]))
    @classmethod
    def get_tournament_by_name(cls, tournament_name,db):
        tournament_table = db.table('Tournament')
        tournament_all =  tournament_table.all()
        for tournament in tournament_all:
            key_ = list(tournament.keys())[0]
            if tournament[key_] == tournament_name:
                return tournament
        return None
    @classmethod
    def get_match_tournament(cls, tournament_name, status, db):
        list_match = []
        tourn = cls.get_tournament_by_name(tournament_name, db)
        if tourn:
            matchs = tourn['Rounds'][-1]['Match']
            print('matchs', matchs)
            for match  in matchs:
                if match['Status'] == status:
                    list_match.append(match)
            return list_match




    """@classmethod
    def run_tournament(cls, tournament_name, db):
        t_dict = cls.get_tournament_by_name(tournament_name, db)
       
        if t_dict:
            matchs = t_dict['Rounds'][-1]['Match']
            for i, m in enumerate(matchs):
                print(" ")#
                print(f"     The match that has:\n{m['Player 1']} vs {m['Player 2']} \n has ended and the winner is:")
                print(" ")#
                score_p1 = float(input(f"Entre the score of {m['Player 1']}: "))
                score_p2 = float(input(f"Entre the score of {m['Player 2']}: "))
                m['Score']= (score_p1, score_p2)
                t_dict['Rounds'][-1]['Match'][i] = m
                print(m) 
                
        else:
            print("The tournament you are looking for does't exist in our database")"""




    @classmethod
    def run_tournament(cls, tournament_name, db):
        #list_of_finished_match = []
        t_dict = cls.get_tournament_by_name(tournament_name, db)

        if t_dict:
            matchs = t_dict['Rounds'][-1]['Match']
            for i, m in enumerate(matchs):
               
                score_p1 = float(input(f"Entre the score of {m['Player 1']}: "))
                score_p2 = float(input(f"Entre the score of {m['Player 2']}: "))
                m['Score']= (score_p1, score_p2)
                
                status = input("Has this match ended? Enter 'y' for Yes: ")
                if status.lower() == 'y':
                    m ['Status'] = "Ended"
                else:
                    m ['Status'] = "Paused"

                t_dict['Rounds'][-1]['Match'][i] = m

                print(" ")#
                print(f"                 The detail and score of the match that has:\n                        {m['Player 1']} vs {m['Player 2']} \n                                 is:")
                print(" ")#

            print(t_dict) 
            tn_name = input('please enter the name of tournament which you want to display their match: ')
            st = input('Which status: ')
            match = cls.get_match_tournament(tn_name, st, db)
            print(match)
            #DatabaseWorker.save_tournament_in_db(tournament, t_dict, db)# To do
                    
        else:
            #list_of_finished_match.append([m['Player 1'], score_p1], [m['Player 2'], score_p2])      
            print("The tournament you are looking for does't exist in our database")
            
        print(t_dict)
        
    
class TournamentReport:

    def __call__(self):  #, dict_tournament, list_player, db, tdb

        db = TinyDB('data_base.json')
        Player = Query()
        Table_player = db.table('Player')
        tdb = TinyDB('tournament_db.json')

        self.menu_create = create_menu.CreateMenu()
        self.main_menu_controller = menu_controller.MainMenuController()
        self.display_player = display_menu.DisplayPlayersReport()
        self.display_tournament = display_menu.DisplayTournamentsReport()
        self.display_player_by_tournament = display_menu.DisplayPlayersByTournament()
        serialized_player_table = db.table('Player')
        self.players_db = serialized_player_table.all()

        self.serialized_tournament_table = tdb.table('Tournament')
        self.dict_tournament = self.serialized_tournament_table.all()
        

        serialized_tournament_table = tdb.table('Tournament')
        self.all_tournament = serialized_tournament_table.all()
  
        
       
       
        """self.display_tournament(self.all_tournament )
        identifiant_tournament = input("Enter Tournament  : ")
        choice_tournament = self.all_tournament[int(identifiant_tournament)-1]
        print(choice_tournament)"""

        # Display all the tournaments
        #self.display_tournament(self.all_tournament)
        #self.display_tournament(self.dict_tournament)
        entry = self.menu_create(self.menu_create.tournaments_report_menu)
        while True:
            
            if entry == "1":
                self.display_tournament(self.all_tournament)
               # self.display_tournament = self.main_menu_controller(self.all_tournament, self.players_db, db, tdb)  #self.all_tournament, self.players_db, db, tdb
                input("Enter a letter to returne to Main Menu")
                TournamentReport.__call__(self)
            # Choose a tournament
            if entry == "2":
                identifiant_tournament = input("Enter Tournament  : ")
                choice_tournament = self.all_tournament[int(identifiant_tournament)-1]
                print(
                    f"Tournament Id:", identifiant_tournament,
                    "Tournament name:", choice_tournament['Tournament name'], 
                    "Venue:", choice_tournament['Venue'],
                    "Date:", choice_tournament['Date'],
                    "Time-Control:", choice_tournament['Time-Control'],
                    "Number of Players:", choice_tournament['Number of players'],
                    "Number of Rounds:", choice_tournament['Number of Rounds']                 
                    )
                input("Enter any letter to returne to Main Menu: ")
                TournamentReport.__call__(self)
                #self.menu_create()
                # To print the dictionary of the tournament
                #print(choice_tournament)
            else:
                entry = self.menu_create(self.menu_create.sub_tournaments_report_menu)
                # Display the players in the chosen Tournament in alphabetical order
                if entry == "1":
                    entry = self.menu_create(self.menu_create.players_report_menu)
                if entry == "1":
                    #identifiant_tournament = input("Enter Tournament  : ")
                    choice_tournament = self.all_tournament[int(identifiant_tournament)-1]
                    list_player_ = [(p['Last name'], p['First name'], p['Rank']) for p in choice_tournament['Players']]
                    self.display_player_by_tournament(sorted(list_player_, key = lambda x: x[0]))
                    input("Enter any letter to returne to Main Menu: ")
                    TournamentReport.__call__(self)

                # Display the players in the chosen Tournament in ranking order
                if entry == "2":
                    self.display_player_by_tournament(sorted(list_player_, key = lambda x: x[2],reverse=True))
                    TournamentReport.__call__(self)

                # Display the Rounds in the chosen Tournament
                if entry == "2":
                    print([(r['Round name'], 
                    r['Start date'], 
                    r['End date'] ) 
                    for r in list(choice_tournament['Rounds'])])
                    input("Enter any letter to returne to Main Menu: ")
                    TournamentReport.__call__(self)

                if entry == "3":
                    print([r['Match'] for r in choice_tournament['Rounds']])
                    input("Enter any letter to returne to Main Menu: ")
                    TournamentReport.__call__(self)


                    # Go to main menu
                if entry == "4":
                    valid_choice = False
                    self.main_menu_controller()






                    
                    """list_player_ = [(p['Last name'], p['First name'], p['Rank']) for p in choice_tournament['Players']]
                    self.display_player_by_tournament(sorted(list_player_, key = lambda x: x[0]))
                    print('=====================================')
                    self.display_player_by_tournament(sorted(list_player_, key = lambda x: x[2],reverse=True))
                    print('==============Round===============')
                    print(" ")
                    print([(r['Round name'], r['Start date'], r['End date'] ) for r in list(choice_tournament['Rounds'])])
                    print("")
                    print(" ")
                    print('============== Match ===============')
                    print("")
                    print([r['Match'] for r in choice_tournament['Rounds']])
                    print("")"""

                

        
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
    
            # Go to main menu
            if entry == "2":

                self.main_menu_controller()

            print("Enter the number corresponding to the choice you want")  
        
 
        

