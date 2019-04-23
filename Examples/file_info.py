from pprint import pprint

from NexusWrapper.nexus import Nexus

nexus = Nexus()
mod = nexus.file_info('Fallout76', 84, 378)
pprint(mod)
