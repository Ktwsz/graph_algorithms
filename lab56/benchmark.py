from utils import lexbfs as lex_fast, parse_graph
from utils_slow import lexbfs as lex_slow
from time import process_time
from dimacs import loadWeightedGraph
from os import listdir


def run_with_time(func, G, s):
    timer_start = process_time()
    _ = func(G, s)
    timer_stop = process_time()

    return timer_stop - timer_start


def gen_custom_graph():
    N = int(5 * 1e3)

    out = []
    for i in range(1, N+1):
        for j in range(i+1, N+1):
            out.append([i, j, 1])

    return out


if __name__ == '__main__':
    TEST_DIR = 'chordal'
    print("time fast", "time slow")
    s = 0
    for file in listdir(TEST_DIR):
        n, E = loadWeightedGraph(TEST_DIR + '/' + file)
        G = parse_graph(E, n)

        time1 = run_with_time(lex_fast, G, s)
        time2 = run_with_time(lex_slow, G, s)

        print(time1-time2)

    G = parse_graph(gen_custom_graph(), int(5 * 1e3))
    time1 = run_with_time(lex_fast, G, s)
    print("done1")
    time2 = run_with_time(lex_slow, G, s)
    print("done2")


    print(time1 - time2)
