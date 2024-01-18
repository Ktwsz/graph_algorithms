from dimacs import *
from os import listdir, popen
import sys

from planar import solve as planar_solve
from flow import solve as flow_solve
from sat import solve as sat_solve

TEST_DIRS = {
    "planar": ("planar", loadWeightedGraph, planar_solve),
    "flow": ("flow", loadDirectedWeightedGraph, flow_solve),
    "sat": ("sat", loadCNFFormula, sat_solve),
}


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


def fancy_print(left, right):
    _, width = popen('stty size', 'r').read().split()
    width = int(width)
    print('{}{}{}'.format(left, ' '*(width-len(left+right)), right))


def test_single(test_dir, test_file, load_test_func, test_func):
    file_path = test_dir + "/" + test_file
    n, E = load_test_func(file_path)

    res = test_func(E, n)

    if test_dir == "sat":
        solution = int(readCNNSolution(file_path))
    else:
        solution = int(readSolution(file_path))

    if solution == res:
        print(f"{bcolors.OKGREEN}OK {test_file}{bcolors.ENDC}")
    else:
        fancy_print(f"{bcolors.FAIL}WA {test_file}{bcolors.ENDC}", f"[{bcolors.WARNING}{res}{bcolors.ENDC} | {bcolors.OKGREEN}{solution}{bcolors.ENDC}]")


def test_directory(test_dir, load_test_func, test_func):
    print(f"{bcolors.OKBLUE} TESTING {test_dir}{bcolors.ENDC}")
    for test_file in listdir(test_dir):
        test_single(test_dir, test_file, load_test_func, test_func)


def test_all():
    for args in TEST_DIRS.values():
        test_directory(*args)


if __name__ == '__main__':
    test_key = sys.argv[1]
    test_file = None if len(sys.argv) < 3 else sys.argv[2]

    if test_key == "all":
        test_all()
    elif test_key in TEST_DIRS:
        test_dir, test_load_func, test_func = TEST_DIRS[test_key]

        if test_file is None:
            test_directory(test_dir, test_load_func, test_func)
        else:
            test_single(test_dir, test_file, test_load_func, test_func)
