from networkx import Graph, DiGraph


def check_evaluation(formula, evaluation):
    for x1, x2 in formula:
        if x1 < 0:
            value_x1 = not evaluation[-x1]
        else:
            value_x1 = evaluation[x1]

        if x2 < 0:
            value_x2 = not evaluation[-x2]
        else:
            value_x2 = evaluation[x2]

        if not (value_x1 or value_x2):
            return False

    return True


def parse_graph_directed(E, n):
    G = DiGraph()
    G.add_nodes_from(range(n))

    for u, v, w in E:
        u, v = u - 1, v - 1
        G.add_edge(u, v)
        G[u][v]['capacity'] = w

    return G


def parse_graph_undirected(E, n):
    G = Graph()
    G.add_nodes_from(range(n))

    for u, v, _ in E:
        u, v = u - 1, v - 1
        G.add_edge(u, v)

    return G


def parse_graph_cnn(E, n):
    G = DiGraph()
    nodes = [[-i, i] for i in range(1, n + 1)]
    G.add_nodes_from([i for j in nodes for i in j])

    for u, v in E:
        G.add_edge(-u, v)
        G.add_edge(-v, u)

    return G
