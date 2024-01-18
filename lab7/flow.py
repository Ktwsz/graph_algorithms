from networkx.algorithms.flow import maximum_flow
from utils import parse_graph_directed


def solve(E, n):
    G = parse_graph_directed(E, n)
    s, t = 0, n-1
    return maximum_flow(G, s, t)[0]
