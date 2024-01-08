from os import listdir
from dimacs import loadWeightedGraph


class LinkedNode:
    def __init__(self, id=None, v=None):
        self.values = {v} if v else set()
        self.previous = None
        self.next = None
        self.id = id

    def add(self, v):
        self.values.add(v)

    def pop(self):
        return self.values.pop()

    def isEmpty(self):
        return len(self.values) == 0

    def split(self, v):
        if v not in self.values:
            return None

        self.values.remove(v)

        result = None

        if self.next is None or self.next.id != self.id:
            tmp = LinkedNode(self.id, v)

            tmp.next = self.next
            tmp.previous = self

            if self.next:
                self.next.previous = tmp

            self.next = tmp
            result = tmp
        else:
            self.next.add(v)
            result = self.next

        if not self.values:
            if self.next:
                self.next.previous = self.previous
            if self.previous:
                self.previous.next = self.next

        return result


class LinkedArray:
    def __init__(self, first, second):
        self.head = LinkedNode(id=0)
        self.head.values = first

        self.tail = LinkedNode(id=1)
        self.tail.values = second

        self.head.next = self.tail
        self.tail.previous = self.head

        self.id = 2

    def pop(self):
        result = self.tail.pop()

        if self.tail.isEmpty():
            self.tail = self.tail.previous
            if self.tail:
                self.tail.next = None

        return result

    def isEmpty(self):
        return self.tail is None

    def updateEnds(self):
        if self.head.isEmpty():
            self.head = self.head.next
        if self.tail and self.tail.next is not None:
            self.tail = self.tail.next

    def getNewId(self):
        self.id += 1
        return self.id - 1

    def __repr__(self):
        tmp = self.head
        s = ""

        while tmp is not None:
            s += str({v+1 for v in tmp.values})
            tmp = tmp.next
        return s


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

    que = LinkedArray({v for v in range(n) if v != s}, {s})
    links = [que.head if v != s else que.tail for v in range(n)]
    vis = []

    ctr = 0
    while not que.isEmpty():
        u = que.pop()

        vis.append(u)

        for v in G[u].out:
            new_link = links[v].split(v)
            links[v] = new_link or links[v]

        for v in G[u].out:
            links[v].id = que.getNewId()

        que.updateEnds()
        ctr += 1

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
