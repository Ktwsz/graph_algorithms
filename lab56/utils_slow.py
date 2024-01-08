from os import listdir
from dimacs import loadWeightedGraph


class Node:
    def __init__(self, idx):
        self.idx = idx
        self.out = set()

    def connect_to(self, v):
        self.out.add(v)

    def __eq__(self, other):
        return self.idx == other.idx

    def __hash__(self):
        return hash(self.idx)


def parse_graph(E, n):
    G = [Node(i) for i in range(n)]

    for u, v, _ in E:
        u, v = u - 1, v - 1
        G[u].connect_to(v)
        G[v].connect_to(u)

    return G


def lexbfs(G, s):
    n = len(G)

    que = [{u for u in range(n) if u != s}, {s}]
    vis = []

    while que:
        u = que[-1].pop()
        neighbours = G[u].out

        vis.append(u)

        new_que = []
        for X in que:
            Y = X & neighbours
            K = X - Y
            if K:
                new_que.append(K)
            if Y:
                new_que.append(Y)

            que = new_que

    return vis


def get_RN(G):
    n = len(G)

    vis = lexbfs(G, 0)
    RN = [(set(), -1) for _ in range(n)]

    s = {vis[0]}
    for ix, u in enumerate(vis[1:]):
        ix += 1
        neigh = s & G[u].out

        parent = -1
        for i in vis[:ix][::-1]:
            if i in neigh:
                parent = i
                break

        RN[u] = (neigh, parent)

        s.add(u)

    return RN


def checkLexBFS(G, vs):
    n = len(G)
    pi = [None] * n
    for i, v in enumerate(vs):
        pi[v] = i

    for i in range(n-1):
        for j in range(i+1, n-1):
            Ni = G[vs[i]].out
            Nj = G[vs[j]].out

            verts = [pi[v] for v in Nj - Ni if pi[v] < i]
            if verts:
                viable = [pi[v] for v in Ni - Nj]
                if not viable or min(verts) <= min(viable):
                    return False
    return True


if __name__ == '__main__':
    TEST_DIR = 'chordal'
    for file in listdir(TEST_DIR):
        n, E = loadWeightedGraph(TEST_DIR + '/' + file)
        G = parse_graph(E, n)
        result = checkLexBFS(G, lexbfs(G, 0))

        print(f"TEST {file} result: {result}")
        exit()
