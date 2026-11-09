"""pääohjelma"""
import requests
from player import Player

class PlayerReader:
    """Pelaajien lukija"""
    def __init__(self, url):
        """init"""
        self.url = url

    def get_players(self):
        """pelaajien haku"""
        response = requests.get(self.url, timeout=10).json()

        players = []

        for player_dict in response:
            player = Player(player_dict)
            players.append(player)

        return players

    def get_sorted_players_by_points(self, players):
        """pelaajien järjestäminen pisteiden mukaan"""
        sorted_players = sorted(players, key=lambda p: (p.pisteet, p.goals), reverse = True)

        return sorted_players

class PlayerStats:
    """pelaajatilastoluokka"""
    def __init__(self, reader):
        """init"""
        self.reader = reader
        self.players = reader.get_players()

    def players_by_nationality(self, nationality):
        """pelaajien kanssallisuuden haarukointi"""
        filtered_players = [p for p in self.players if p.nationality == nationality]

        return filtered_players

    def top_scorers_by_nationality(self, nationality):
        """pelaajien printtaus kansallisuuden mukaan"""
        matched_players = self.players_by_nationality(nationality)

        top_scorers = self.reader.get_sorted_players_by_points(matched_players)

        return top_scorers

def main():
    """main"""
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")

    for player in players:
        print(player)
