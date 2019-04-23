from pprint import pprint

from NexusWrapper.nexus import Nexus

nexus = Nexus()
mod = nexus.file_list('Fallout76', 84)
pprint(mod)
