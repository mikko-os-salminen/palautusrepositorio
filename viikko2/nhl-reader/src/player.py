"""pelaajaluokan määrittely"""
class Player:
    """Pelaajaluokka"""
    def __init__(self, pdict):
        """initin määrittely"""
        self.name = pdict['name']
        self.nationality = pdict['nationality']
        self.team = pdict['team']
        self.goals = pdict['goals']
        self.assists = pdict['assists']

    def get_pisteet(self):
        """pisteiden lasku"""
        pisteet = self.goals + self.assists
        return pisteet

    def __str__(self):
        """tiedot stringinä takas"""
        return (
            f"{self.name:20} {self.team:15} {self.goals:2} "
            f"+ {self.assists:3} = {self.get_pisteet()}"
        )
