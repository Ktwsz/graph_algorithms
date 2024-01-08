from utils import parse_graph, lexbfs


def coloring_solve(E, n):
    G = parse_graph(E, n)

    vis = lexbfs(G, 0)
    colors = [0 for _ in range(n)]
    possible_colors = {i for i in range(1, n+1)}

    for u in vis:
        colors[u] = min(possible_colors - {colors[v] for v in G[u].out})

    return max(colors)
