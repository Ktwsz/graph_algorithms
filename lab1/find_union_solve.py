from math import inf

def find_set(u):
    global parent

    if parent[u] != u:
        parent[u] = find_set(parent[u])
    return parent[u]

def union_set(u, v):
    global parent
    global rank

    u = find_set(u)
    v = find_set(v)

    if rank[u] > rank[v]: 
        parent[v] = u
    else:
        parent[u] = v
        if rank[u] == rank[v]:
            rank[v] += 1



def solve(L, n, s, t):
    global parent
    global rank

    if len(L) < n-1:
        return inf

    parent = [i for i in range(n)]
    rank = [0 for _ in range(n)]

    E = [(L[i][2], L[i][0]-1, L[i][1]-1) for i in range(len(L))]
    E.sort(reverse=True)
    
    index = 0
    res = inf
    while find_set(s) != find_set(t):
        w, u, v = E[index]
        
        if find_set(u) != find_set(v):
            union_set(u, v)
            res = w

        index += 1

    return res