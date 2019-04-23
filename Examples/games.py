from NexusWrapper.nexus import Nexus

nexus = Nexus()
games = nexus.games()
for game in games:
    name = game['name']
    if name == 'Mafia III':
        print(game)

print(f'There are {len(games)} games on the Nexus right now.')
