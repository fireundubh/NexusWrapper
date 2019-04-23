from pprint import pprint

from NexusWrapper.nexus import Nexus

nexus = Nexus()
game = nexus.game('Fallout76')
pprint(game)
