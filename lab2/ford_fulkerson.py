from collections import deque
from math import inf

def BFS(G, Cf, s, t):
    n = len(G)
    parent = [-1 for _ in range(n)]
    edge_id = [-1 for _ in range(n)]

    q = deque()
    parent[s] = s
    q.append(s)

    while(len(q)):
        u = q.popleft()
        if u == t:
            break

        for v, id in G[u]:
            if parent[v] == -1 and Cf[id] > 0:
                parent[v] = u
                edge_id[v] = id

                q.append(v)

    if parent[t] == -1:
        return None

    new_flow = get_new_flow(Cf, parent, edge_id, s, t)
    update_path(Cf, parent, edge_id, s, t, new_flow)

    return new_flow

def DFS(G, Cf, s, t):
    n = len(G)
    parent = [-1 for _ in range(n)]
    edge_id = [-1 for _ in range(n)]

    def dfs_visit(u):
        for v, id in G[u]:
            if parent[v] == -1 and Cf[id] > 0:
                parent[v] = u
                edge_id[v] = id

                dfs_visit(v)

    parent[s] = s
    dfs_visit(s)

    if parent[t] == -1:
        return None

    new_flow = get_new_flow(Cf, parent, edge_id, s, t)
    update_path(Cf, parent, edge_id, s, t, new_flow)

    return new_flow

def get_new_flow(Cf, parent, edge_id, s, t):
    new_flow = inf
    u = t
    while u != s:
        new_flow = min(new_flow, Cf[edge_id[u]])
        u = parent[u]

    return new_flow

def update_path(Cf, parent, edge_id, s, t, new_flow):
    u = t
    while u != s:
        id = edge_id[u]
        Cf[id] -= new_flow
        Cf[id^1] += new_flow

        u = parent[u]

def max_flow(G, Cf, s, t):
    new_flow = BFS(G, Cf, s, t)

    flow = 0
    while new_flow:
        flow += new_flow
        new_flow = BFS(G, Cf, s, t)

    return flow

def gen_graph(E, n):
    G = [[] for _ in range(n)]
    Cf = [0 for _ in range(len(E)*2)]

    k = 0
    for u, v, w in E:
        u -= 1
        v -= 1

        G[u].append((v, k))
        Cf[k] = w
        k += 1
        
        G[v].append((u, k))
        k += 1

    return G, Cf

def solve(E, n, s, t):
    G, Cf = gen_graph(E, n)

    return max_flow(G, Cf, s, t)

    