class Tournament:
    def __init__(self, name, venue, date, time, rounds):
        self.name = name
        self.venue = venue
        self.date = date
        self.time = time
        self.rounds = rounds

    def __str__(self):
        return f"Tournoi: {self.name}" 

    def __repr__(self):
        
        """Used in print."""
        return str(self)      

