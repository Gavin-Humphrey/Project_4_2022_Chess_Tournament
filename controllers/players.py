from models.players import Player
from views.players import ViewPlayer



class ccontroller_player():

    user_input = ViewPlayer().create_player()

    player = Player(
        user_input['last name'],
        user_input['first name'],
        user_input['dob'],
        user_input['sex'],
        user_input['rank']
        )
         
    player = player.get_player()
    print(player)

