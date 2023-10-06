from dimacs import loadWeightedGraph, readSolution
from os import listdir
#from find_union_solve import solve
#from dfs_solve import solve
from dijkstra_solve import solve

TEST_DIR = "testy"

def test():
    for test_file in listdir(TEST_DIR):
        file_path = TEST_DIR+"/"+test_file
        n, E = loadWeightedGraph(file_path)
        s, t = 0, 1

        res = solve(E, n, s, t)
        ans = int(readSolution(file_path))

        if res == ans:
            print(f"OK TEST {test_file}")
        else:
            print(f"WA TEST {test_file} [res: {res} | ans: {ans}]")

if __name__ == '__main__':
    test()
