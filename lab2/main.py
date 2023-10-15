from dimacs import loadDirectedWeightedGraph as load, readSolution
from os import listdir
from ford_fulkerson import solve

TEST_DIR = "flow"

def test_single(test_file):
    file_path = TEST_DIR+"/"+test_file
    n, E = load(file_path)
    s, t = 0, n-1

    res = solve(E, n, s, t)
    ans = int(readSolution(file_path))

    if res == ans:
        print(f"OK TEST {test_file}")
    else:
        print(f"WA TEST {test_file} [res: {res} | ans: {ans}]")

def test_all():
    for test_file in listdir(TEST_DIR):
        test_single(test_file)

if __name__ == '__main__':
        test_all()
        
