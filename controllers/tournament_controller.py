from cmath import e
from datetime import datetime, date
import re
import time
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
        tournament = Query()
        result = tournament_table.search(tournament['Tournament name']==tournament_name)
        if result:
            return result[0]
        else:
            return

    '''
    tournament_table = db.table('Tournament')
    tournament_all =  tournament_table.all()
    for tournament in tournament_all:
        key_ = list(tournament.keys())[0]
        if tournament[key_] == tournament_name:
            return tournament
    return None
    '''
        
    @classmethod
    def get_match_tournament(cls, tournament_name, status, db):
        list_match = []
        tourn = cls.get_tournament_by_name(tournament_name, db)
        if tourn:
            matchs = tourn['Rounds'][-1]['Match']
            if status == '0':
                list_match = [match for match in matchs if isinstance(match['Score'], list)]
            elif status == '1':
                list_match = [match for match in matchs if isinstance(match['Score'], int)]
            elif status == '2':
                list_match = matchs

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
        tournament_table = db.table('Tournament')
        tournament = Query()

        if t_dict:
            list_player = t_dict['Players']
            matchs = t_dict['Rounds'][-1]['Match']
            r = t_dict['Rounds'][-1]
            all_match_terminated = True
            for i, m in enumerate(matchs):
                if isinstance(m ['Score'], int):
                    all_match_terminated = False
                    response_ = input(f"is the match between {m['Player 1']} and {m['Player 2']} is terminated if yes press 'y' ")
                    if response_.lower() == 'y'  :
                        score_p1 = float(input(f"Entre the score of {m['Player 1']}: "))
                        score_p2 = float(input(f"Entre the score of {m['Player 2']}: "))
                        name_p1 = m['Player 1'].split(' ')
                        last_name_p1 =  name_p1[0]
                        first_name_p1 = name_p1[1]

                        name_p2 = m['Player 2'].split(' ')
                        last_name_p2 =  name_p2[0]
                        first_name_p2 = name_p2[1]
                        for p in list_player:
                            if p["Last name"] == last_name_p1 and p['First name'] == first_name_p1:
                                p['Score'] = p['Score'] + score_p1
                            elif p["Last name"] == last_name_p2 and p['First name'] == first_name_p2:
                                p['Score'] = p['Score'] + score_p2
                        m['Score']= tuple([score_p1, score_p2])
                        
                    r['Match'][i] = m
                    tournament_table.update({'Rounds': [r]}, tournament["Tournament name"] == tournament_name)
                    tournament_table.update({'Players': list_player}, tournament["Tournament name"] == tournament_name)
                    

            if all_match_terminated :
                new_r = input('all match are terminated for this round do you wante to start a new round if yes press y: ')
                if new_r.lower() == 'y':
                    cls.add_round(t_dict, tournament_table, tournament, tournament_name)

            #tn_name = input('please enter the name of tournament which you want to display their match: ')
            st = input('Which match status would you display  : ')
            match = cls.get_match_tournament(tournament_name, st, db)
            print(match)
            #DatabaseWorker.save_tournament_in_db(tournament, t_dict, db)# To do         
        else:
            #list_of_finished_match.append([m['Player 1'], score_p1], [m['Player 2'], score_p2])      
            print("The tournament you are looking for does't exist in our database")

        # Important for checking rounds     
    @classmethod
    def add_round(cls, tournament, tournament_table, tournament_query, tournament_name_):
        round_ = tournament['Rounds']
        matchs = round_[-1]['Match']
        is_round_ended = True
        for match in matchs:
            if isinstance(match['Score'],int) :
                is_round_ended = False
                break
        if is_round_ended and len(round_) < tournament["Number of Rounds"]: 
            print("Enter 'Y' to start a new round")
            choice = input(": ")
            if choice.lower() == "y":
                name_round = input('Please enter the new round name: ')
                round_date_begin = datetime.now().strftime("%d/%m/%Y %H:%M")
                list_tournament_player = tournament['Players']
                sort_one_level = sorted (list_tournament_player,key=
                lambda x:(x['Score'], x['Rank']),reverse= True)
                
                list_finale = [ e ['Last name'] +' '+ e ['First name'] for e in cls.ordre_level_three(sort_one_level)]
                list_pair = cls.player_pair(list_finale) 
                list_match = cls.create_matchs(list_pair)

                new_round = Round(name_round,round_date_begin, list_match) 
                round_.append({'Round name': new_round.round_name, "Start date" : new_round.date_begin, "Match":[{'Player 1': m.player1, 'Player 2': m.player2, 'Score': m.score} for m in list_match] } )
                tournament_table.update({'Rounds': round_}, tournament_query["Tournament name"] == tournament_name_)
            
                #was supposed to start here
            elif len(round_) == tournament["Number of Rounds"]:
                print(' vous pouvez pas creer un nouveau round car le nombre de round creer est egale en nombre de round declaree')

            else:
                print('sorry you can not start a new round because the matchs of the last'
                'round were not all terminated')

        
        
        # Create list pair, sorted by score
    @classmethod
    def ordre_level_three(cls, list_player):
        stop = False
        while not stop:
            stop = True
            for i in range(len(list_player) -1):
                if  (list_player[i+1]['Score'] == list_player[i]['Score']) and (list_player[i+1]['Rank'] == list_player[i]['Rank']):
                    if list_player[i+1]['Last name'] < list_player[i]['Last name']:
                        item_indice_i =list_player[i] 
                        list_player[i] = list_player[i+1]
                        list_player[i+1] = item_indice_i
                        stop = False
        return list_player
                        
                    
                
        return list_order



        # @classmethod   
        # def score_order(cls, ditc_player, score):
        #     return ditc_player['Score']
        
        # @classmethod
        # def player_classment_score(cls, list_player, score):
        #     if len(list_player) % 2 != 0:
        #         return "We are sorry we can't start a tournament, the number of players has to be pair"
        #     else:
        #         return [ e ['Last name'] +' '+ e ['First name'] + ' '+ e ['Score'] for e in sorted(list_player, key = score_order, reverse=True)]
        
        # print("hahahahhahhahah")
        # @classmethod
        # def player_pair(cls, player_score_pair):
        #     player_score_pair = player_classment_score()
        #     list_pair = player_score_pair()
        #     if isinstance(player_score_pair, list):
        #         return list(zip(player_pair[:int(len(player_pair)/2)], player_pair[int(len(player_pair)/2):]))
        #     print("Letssss gooooo there!!!!!", player_score_pair)

        #if isinstance(list_player_score, list):
            #return list(zip(list_player_score[:int(len(list_player_score)/2)], list_player_score[int(len(list_player_score)/2):]))


    """@classmethod
    def load_tournament_detail(cls, tournament_name, all_tournament, db):
        # calculate remaining rounds
        t_dict = cls.get_tournament_by_name(tournament_name, db)
        tournament_table = db.table('Tournament')
        display_tournament = display_menu.DisplayTournamentsReport()
        main_menu_controller = menu_controller.MainMenuController()
        round_instances = []
        valid_choice = True 
        if display_tournament:
            while valid_choice:
                identifiant_tournament = input("Enter Tournament ID you want to check round: ")
                choice_tournament = all_tournament[int(identifiant_tournament)-1]
                for round in choice_tournament['Rounds']:
                    serialized_round = tournament_table.get(doc_id=round)
                    round_instances.append(serialized_round)
                    choice_tournament['Rounds'] = round_instances
                    tournament_object = all_tournament(choice_tournament)

            else:
                print("Pas de tournoi en cours, retour au menu principal")
                time.sleep(1)
                main_menu_controller()"""
        
      
    
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
        if entry == "1":
            self.display_tournament(self.all_tournament)
            ##
            tournament_display_info = self.display_tournament(self.all_tournament)
            '''
            print()
            all_tournament_disp_info = [
                tournament_display_info['Tournament ID'],
                tournament_display_info['Tournament name'],
                tournament_display_info['Venue'],
                tournament_display_info['Date']
            ]
            self.display_tournament.display_all_tournament_info(all_tournament_disp_info)
            
            
            '''
            
            ##
            # self.display_tournament = self.main_menu_controller(self.all_tournament, self.players_db, db, tdb)  #self.all_tournament, self.players_db, db, tdb
            input("Enter a letter to returne to Main Menu")
            TournamentReport.__call__(self)
            # Choose a tournament
        if entry == "2":
            valid_choice = True 
            while valid_choice:
                identifiant_tournament = input("Enter Tournament ID : ")
                choice_tournament = self.all_tournament[int(identifiant_tournament)-1]
                tournament_sel = [
                    identifiant_tournament,
                    choice_tournament['Tournament name'], 
                    choice_tournament['Venue'],
                    choice_tournament['Date'],
                    choice_tournament['Time-Control'],
                    choice_tournament['Number of players'],
                    choice_tournament['Number of Rounds']]
                self.display_tournament.display_tournament_sel(tournament_sel)
                """print(
                    f"Tournament Id:", identifiant_tournament,
                    "Tournament name:", choice_tournament['Tournament name'], 
                    "Venue:", choice_tournament['Venue'],
                    "Date:", choice_tournament['Date'],
                    "Time-Control:", choice_tournament['Time-Control'],
                    "Number of Players:", choice_tournament['Number of players'],
                    "Number of Rounds:", choice_tournament['Number of Rounds']                 
                    )"""
                input("Enter any letter to returne to Main Menu: ")
                #TournamentReport.__call__(self)
              
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
                    input("Enter any letter to returne to Main Menu: ")
                    #TournamentReport.__call__(self)
 
                    # Display the players in the chosen Tournament in ranking order
                    entry = self.menu_create(self.menu_create.players_report_menu)
                    if entry == "2":
                        choice_tournament = self.all_tournament[int(identifiant_tournament)-1]
                        self.display_player_by_tournament(sorted(list_player_, key = lambda x: x[2],reverse=True))
                        input("Enter any letter to returne to Main Menu: ")   
                        #TournamentReport.__call__(self)
                       
                # Display the Rounds in the chosen Tournament
                entry = self.menu_create(self.menu_create.sub_tournaments_report_menu)
                if entry == "2":
                    print(choice_tournament['Rounds'])
                    l_round_choice = [(r['Round name'], r['Start date'], r['End date'] )  
                    for r in choice_tournament['Rounds']]
                    print(l_round_choice)

                    input("Enter any letter to returne to Main Menu: ")
                    #TournamentReport.__call__(self)

                # Display the matches in chosen Tournament   
                entry = self.menu_create(self.menu_create.sub_tournaments_report_menu)
                if entry == "3":
                    print([r['Match'] for r in choice_tournament['Rounds']])
                    input("Enter any letter to returne to Main Menu: ")
                    #TournamentReport.__call__(self)

                    # Go to main menu
                if entry == "4":
                    valid_choice = False
                    TournamentReport.__call__(self)
                    self.main_menu_controller(self)






                
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

        else:    # Go to main menu
            if entry == "3":
                valid_choice = False
                self.main_menu_controller()

            print("Enter the number corresponding to the choice you want")  
        
 
        

