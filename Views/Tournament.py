from Controllers.TournamentTime import get_timestamp

class CreateTournament:
    
    def show_content(self):

        date = get_timestamp()

        print("We have a new tournament today:" +date)

        time = input("At:\n >")

        name = input("Tournament name:\n> ")

        venue = input("Venue:\n> ")

        rounds = input("Rounds:\n> ")

        return {
                "date": date,
                "time": time,
                "name": name,
                "venue": venue,
                "rounds": rounds
        }




