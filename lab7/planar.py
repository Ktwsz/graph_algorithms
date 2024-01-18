from networkx import check_planarity
from utils import parse_graph_undirected


def solve(E, n):
    return check_planarity(parse_graph_undirected(E, n))[0]
