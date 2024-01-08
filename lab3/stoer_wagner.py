from heapq import heappop, heappush, heapify
from copy import deepcopy


class Node:
    def __init__(self):
        self.edges = {}
        self.is_merged = False
        self.edges_sum = 0

    def add_edge(self, v, weight):
        self.edges[v] = self.edges.get(v, 0) + weight
        self.edges_sum += weight

    def del_edge(self, v):
        self.edges_sum -= self.edges[v]
        del self.edges[v]

    def get_edge(self, v):
        return self.edges[v]


def minimumCutPhase(G, n, edges_sum, start_v):
    s = [start_v]

    que = [(-edges_sum[i], i) for i in range(len(G)) if i != start_v and not G[i].is_merged and edges_sum[i] != 0]
    heapify(que)

    while len(s) < n:
        _, next_v = heappop(que)
        while G[next_v].is_merged:
            _, next_v = heappop(que)

        merge_vertices(G, start_v, next_v, edges_sum, que)
        s.append(next_v)

    return (s[-1], s[-2])


def minimumCut(G, s):
    n = len(G)

    start_v = s

    mincut = G[s].edges_sum

    while n > 1:
        edges_sum = [0 for _ in range(len(G))]
        for vert, weight in G[s].edges.items(): edges_sum[vert] = weight

        u, v = minimumCutPhase(deepcopy(G), n, edges_sum, start_v)

        mincut = min(mincut, G[u].edges_sum)

        merge_vertices(G, u, v, edges_sum, None)

        n -= 1

    return mincut


def merge_vertices(G, u, v, edges_sum, que):
    if v in G[u].edges:
        G[u].del_edge(v)

    for vert, weight in G[v].edges.items():
        if vert == u:
            continue

        G[u].add_edge(vert, weight)
        G[vert].del_edge(v)
        G[vert].add_edge(u, weight)

    G[v].is_merged = True

    if que is None: return

    for vert, weight in G[u].edges.items():
        if edges_sum[vert] == weight: continue
        edges_sum[vert] = weight
        heappush(que, (-weight, vert))


def gen_graph(E, n):
    G = [Node() for _ in range(n)]

    for u, v, w in E:
        u -= 1
        v -= 1

        G[u].add_edge(v, w)
        G[v].add_edge(u, w)

    return G


def solve(E, n):
    s = 0

    G = gen_graph(E, n)

    return minimumCut(G, s)
