from pprint import pprint

from NexusWrapper.nexus import Nexus

nexus = Nexus()
mod = nexus.search('Recipes and Plans Glow')
pprint(mod)
