from utils import lexbfs, parse_graph


def vcover_solve(E, n):
    G = parse_graph(E, n)

    vis = lexbfs(G, 0)[::-1]

    I = set()

    for u in vis:
        N = G[u].out

        if not I & N:
            I.add(u)

    return n - len(I)
