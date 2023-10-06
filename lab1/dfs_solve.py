from math import inf
from queue import Queue as que

def gen_graph(E, n):
    G = [[] for _ in range(n)]

    for u, v, w in E:
        u -= 1
        v -= 1
        G[u].append((v, w))
        G[v].append((u, w))

    return G

def path_exists(G, s, t, weight_limit):
    n = len(G)
    visited = [False for _ in range(n)]
    visited[s] = True
        
    q = que()
    q.put(s)
    
    while not q.empty():
        u = q.get()

        for v, w in G[u]:
            if w >= weight_limit and not visited[v]:
                visited[v] = True
                q.put(v)

    return visited[t]

def solve(E, n, s, t):
    if len(E) < n-1:
        return inf
    
    G = gen_graph(E, n)
    weight = [E[i][2] for i in range(len(E))]
    weight.sort()

    l, r = 0, len(weight)

    while r-l > 1:
        m = (l+r)//2

        if path_exists(G, s, t, weight[m]):
            l = m
        else:
            r = m

    return weight[l]
