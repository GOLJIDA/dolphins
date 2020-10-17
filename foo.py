import networkx as nx

gml = nx.read_gml('dolphins.gml')

nx.draw(gml)