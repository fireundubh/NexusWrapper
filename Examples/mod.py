from pprint import pprint

from NexusWrapper.nexus import Nexus

nexus = Nexus()
mod = nexus.mod('Fallout76', 84)
pprint(mod)
