from pprint import pprint

from NexusWrapper.nexus import Nexus

nexus = Nexus()

md5 = nexus.calc_md5('Examples\\glow-loose-84-1-5-1543597528.7z')

mod = nexus.get_file_by_md5('Fallout76', md5)
pprint(mod)
