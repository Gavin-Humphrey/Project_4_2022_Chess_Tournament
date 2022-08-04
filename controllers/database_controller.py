from tinydb import  TinyDB, Query, where

#from tinydb import where
#import models.players
#from models.tournament import Tournament
#from models.match import Match


class DatabaseWorker:
    @classmethod
    def get_player_by_name(cls, last_name_, first_name_, db):
        list_found = []
        #Player = Query()#
        table_player = db.table('Player')
        list_all_player= table_player.all()
       # print('all',list_all_player  )#
        for player in list_all_player:
            if player['Last name'] == last_name_ and player['First name'] == first_name_:
                list_found.append(player)
                return player, list_found
        return None, list_found 
        
    @classmethod
    def save_player_in_db(cls, list_player, db):
        serialized_player_table = db.table('Player')
        choice = input('Would you like to eraze the content of this table? Type Y for yes ')
        if choice == 'Y':
            serialized_player_table.truncate()
        for p in list_player:
            p_,lf = cls.get_player_by_name(p.last_name, p.first_name, db)
            if not lf:
                serialized_player_table.insert({'Last name':p.last_name, 'First name': p.first_name, 'Date of birth': p.dob, 'Gender':p.gender, 'Rank':p.rank, 'Score':p.score})
            else:
                print(f"This pLayer: {p.last_name} {p.first_name}, already exist in our database")

    @classmethod
    def save_tournament_in_db(cls, tournament, db):
        #save_tournament(create_tournament(), serialized_tournament_table)
        #get_all_tournament(serialized_tournament_table.all())
        dict_tournament = {}
        serialized_tournament_table = db.table('Tournament')
     
        dict_tournament ['Tournament name'] = tournament.name
        dict_tournament ['Venue'] = tournament.place
        dict_tournament ['Date'] = tournament.date
        dict_tournament ['Time-Control'] = tournament.time_control
        dict_tournament ['Descrition'] = tournament.desc
        dict_tournament ['Number of Rounds'] = tournament.nb_rounds
        list_round = []
        for e in tournament.rounds:
            list_match = []
            list_round.append({'Round name': e.round_name, "Start date" : e.date_begin, "End date": e.date_end})
            for m in e.list_match:
               # list_match.append({'Player 1': m.player1, 'Player 2': m.player2, 'Score': m.score, 'Status':m.status})
                list_match.append({'Player 1': m.player1, 'Player 2': m.player2, 'Score': m.score})
            list_round[-1]["Match"] = list_match
        dict_tournament ['Rounds'] = list_round
        dict_tournament ['Number of players'] = tournament.nb_player
        dict_tournament ['Players'] = tournament.players
        serialized_tournament_table.insert(dict_tournament)#

   # To do
    """def update_db(db, serialized_player_table):
        db = TinyDB("data_base.json")
        db.update(
            serialized_player_table,
            where('Las name') == serialized_player_table['Last name']
        )
        print(f"{serialized_player_table['Last name']} up dated!")


    def update_player_rank(db, serialized_player_table):
        db = TinyDB("data_base.json")
        db.update(
                {'Rank': serialized_player_table['Rank'], 'Score': serialized_player_table['Score']},
                where('Last name') == serialized_player_table['Last name']
        )"""
       
    """def save_tournament(tournment_list, serialized_tournament_table):
        truncate_choice = input("Would you like to clear off tournament? type Y for yes ")
        if truncate_choice == 'Y':
            serialized_tournament_table.truncate()
        for t in tournment_list:
            serialized_tournament_table.insert({'Tournament':t.name, 'Venue': t.place, 'Date': t.date, 'Time': t.time, 'Players': t.players})#"""





