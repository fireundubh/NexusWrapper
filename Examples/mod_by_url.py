from pprint import pprint

from NexusWrapper.nexus import Nexus

nexus = Nexus()
mod = nexus.mod_by_url('https://www.nexusmods.com/fallout76/mods/84')
pprint(mod)
