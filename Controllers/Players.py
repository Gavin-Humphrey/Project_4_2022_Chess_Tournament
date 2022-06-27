from Models.Players import Player
from Views.Players import CreatePlayer

class create_player():

    user_input = CreatePlayer().display_input()

    player = Player(
        user_input['last name'],
        user_input['first name'],
        user_input['dob'],
        user_input['sex'],
        user_input['rank']
        )

    # Serializing created player          
    serialized_player = player.get_serialized_player()
    print(serialized_player)

