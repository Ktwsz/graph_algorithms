from utils import parse_graph, get_RN


def chordal_solve(E, n):
    G = parse_graph(E, n)

    RN = get_RN(G)
    for ix, (u_RN, parent) in enumerate(RN):
        if parent == -1:
            continue

        parent_RN, _ = RN[parent]
        if not u_RN - {parent} <= parent_RN:
            return 0

    return 1
