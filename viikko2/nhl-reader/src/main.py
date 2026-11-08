import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        self.url = url

    def get_players(self):
        response = requests.get(self.url).json()

        players = []
        
        for player_dict in response:
            player = Player(player_dict)
            players.append(player)

        return players

class PlayerStats:
    def __init__(self, reader):
        self.players = reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        filtered_players = [p for p in self.players if p.nationality == nationality]
        filtered_players.sort(key=lambda p: (p.pisteet, p.goals), reverse = True)
    
        return filtered_players

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")

    for player in players:
        print(player)



