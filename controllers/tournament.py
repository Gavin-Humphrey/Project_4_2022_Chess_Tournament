from models.tournament import Tournament
from views.tournament import CreateTournament


class create_tournament():
    
    user_input = CreateTournament().show_content()

    tournament = Tournament(
        user_input['name'],
        user_input['venue'],
        user_input['date'],
        user_input['time'],
        user_input['rounds']
    )  
    

