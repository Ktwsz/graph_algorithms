from networkx.algorithms.components import strongly_connected_components as scc
from networkx.algorithms.dag import topological_sort
from networkx import DiGraph
from utils import parse_graph_cnn, check_evaluation

def check_solvable(SCC):
    for s in SCC:
        for x in s:
            if -x in s:
                return False
    return True


def get_scc_graph(SCC, G):
    SCC_G = DiGraph()
    SCC_G.add_nodes_from(range(len(SCC)))

    def add_edge_set(s1, ix1, s2, ix2):
        for e1 in s1:
            for e2 in s2:
                if G.has_edge(e1, e2):
                    SCC_G.add_edge(ix1, ix2)
                    return


    for ix1, s1 in enumerate(SCC):
        for ix2, s2 in enumerate(SCC):
            if ix1 == ix2:
                continue

            add_edge_set(s1, ix1, s2, ix2)

    return SCC_G


def solve(E, n):
    G = parse_graph_cnn(E, n)
    nodes = scc(G)
    SCC = [s for s in nodes]

    if not check_solvable(SCC):
        return False

    SCC_G = get_scc_graph(SCC, G)

    sorted_SCC_G = topological_sort(SCC_G)
    evaluation = [None for _ in range(n + 1)]
    for s in sorted_SCC_G:
        for x in SCC[s]:
            is_neg = x < 0
            x = abs(x)
            if evaluation[x] is None:
                evaluation[x] = is_neg
            else:
                value = evaluation[x]
                if is_neg:
                    value = not value

                if value == False:
                    evaluation[x] = is_neg


    return check_evaluation(E, evaluation)
