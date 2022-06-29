from Controllers.TournamentTime import get_timestamp

class CreateTournament:
    
    def show_content(self):

        print("Create Tournament")
  
        date = input("Date (DD/MM/YYYY):\n> ")

        time = input("Time (H:M):\n > ")

        name = input("Tournament name:\n> ")

        venue = input("Venue:\n> ")

        rounds = input("Rounds:\n> ")

        print(f"{name} Tournament is created!")

        return {
                "date": date,
                "time": time,
                "name": name,
                "venue": venue,
                "rounds": rounds
        }




