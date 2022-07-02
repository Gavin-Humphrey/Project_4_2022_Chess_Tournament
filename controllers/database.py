"""from pathlib import Path
from tinydb import TinyDB
from tinydb import where
from views.players import create_player


db = TinyDB('data_base.json')

def save_player_in_db(list_player):
    player_table = db.table('Player')
    choice = input('voulez vous ecraser le contenu de la table player? taper o pour oui ')
    if choice == 'o':
        player_table.truncate()
    for p in list_player:
        player_table.insert({'name':p.name, 'last_name': p.last_name, 'gender':p.gender, 'rank':p.rank, 'score':p.score})
save_player_in_db(create_player())"""

