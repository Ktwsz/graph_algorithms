from dimacs import loadDirectedWeightedGraph as load, readSolution
from os import listdir
from ford_fulkerson import solve

TEST_DIR = "flow"

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def test_single(test_file):
    file_path = TEST_DIR+"/"+test_file
    n, E = load(file_path)
    s, t = 0, n-1

    res = solve(E, n, s, t)
    ans = int(readSolution(file_path))

    if res == ans:
        print(f"{bcolors.OKGREEN}OK TEST {test_file}{bcolors.ENDC}")
    else:
        print(f"{bcolors.FAIL}WA TEST {test_file}{bcolors.ENDC} [res: {bcolors.WARNING}{res}{bcolors.ENDC} | ans: {bcolors.OKGREEN}{ans}{bcolors.ENDC}]")

def test_all():
    for test_file in listdir(TEST_DIR):
        test_single(test_file)

if __name__ == '__main__':
        test_all()
        
