from pprint import pprint

from NexusWrapper.nexus import Nexus

nexus = Nexus()
mods = nexus.new_files('Fallout4')
pprint(mods)
