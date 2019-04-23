from pprint import pprint

from NexusWrapper.nexus import Nexus

nexus = Nexus()
mods = nexus.updated_files('Fallout4')
pprint(mods)
