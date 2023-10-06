from math import inf
from heapq import heappop, heappush


def gen_graph(E, n):
    G = [[] for _ in range(n)]

    for u, v, w in E:
        u -= 1
        v -= 1
        G[u].append((v, w))
        G[v].append((u, w))

    return G

def solve(L, n, s, t):
    if len(L) < n-1:
        return inf

    G = gen_graph(L, n)

    visited = [-1 for _ in range(n)]
    visited[s] = inf

    q = [(inf, s)]

    while len(q) != 0:
        _, u = heappop(q)

        for v, w in G[u]:
            if visited[v] < min(w, visited[u]):
                visited[v] = min(w, visited[u])
                heappush(q, (-visited[v], v))

    return visited[t]

