from tinydb import  Query
#from tinydb import where
#mport models.players
#from models.tournament import Tournament


class DatabaseWorker:
    @classmethod
    def get_player_by_name(cls, last_name_, first_name_,db):
        list_found = []
        #Player = Query()
        table_player = db.table('Player')
        list_all_player= table_player.all()
        #print('all',list_all_player  )
        for player in list_all_player:
            if player['Last name'] == last_name_ and player['First name'] == first_name_:
                list_found.append(player)
                return player,list_found
        return list_found
        

    """def save_player_in_db(list_player, serialized_player_table):
        choice = input('Would you like to eraze the content of this table? Type Y for yes ')
        if choice == 'Y':
            serialized_player_table.truncate()
        for p in list_player:
            serialized_player_table.insert({'Last name':p.last_name, 'First name': p.first_name, 'Date of birth': p.dob, 'Sex':p.sex, 'Rank':p.rank, 'Score':p.score})

    def save_tournament(tournment_list, serialized_tournament_table):
        truncate_choice = input("Would you like to clear off tournament? type Y for yes ")
        if truncate_choice == 'Y':
            serialized_tournament_table.truncate()
        for t in tournment_list:
            serialized_tournament_table.insert({'Tournament':t.name, 'Venue': t.place, 'Date': t.date, 'Time': t.time, 'Players': t.players})"""





