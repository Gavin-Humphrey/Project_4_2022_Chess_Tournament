from Models.Tournament import Tournament
from Views.Tournament import CreateTournament


class create_tournament():
    
    user_input = CreateTournament().show_content()

    tournament = Tournament(
        user_input['name'],
        user_input['place'],
        user_input['date'],
        user_input['time'],
        user_input['rounds']
    )  
    

