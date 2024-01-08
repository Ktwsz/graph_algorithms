from utils import get_RN, parse_graph


def maxclique_solve(E, n):
    G = parse_graph(E, n)

    RN = get_RN(G)

    return max([len(RN[v][0] | {v}) for v in range(n)])
