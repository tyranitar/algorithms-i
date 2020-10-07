from sys import path
from time import time
from sets import Set
path.append('../utils')

from graph_utils import construct_unit_graph, add_unit_directed_reverse, dfs

def format_stupid_string(s):
    s_split = s.split(' ')
    return (int(s_split[0]), int(s_split[1]))

def update_leaders(leaders, i):
    if i not in leaders:
        leaders[i] = 0

    leaders[i] += 1

def kosarajus(al, n):
    n_1 = n + 1

    # First pass.
    g_rvs = construct_unit_graph(al, add_unit_directed_reverse)
    explored = Set()
    finishing_order = []

    for i in range(1, n_1):
        dfs(g_rvs, i, explored, lambda u: finishing_order.append(u))

    # Second pass.
    g = construct_unit_graph(al)
    explored = Set()
    leaders = {}

    for i in reversed(finishing_order):
        dfs(g, i, explored, lambda u: update_leaders(leaders, i))

    return ','.join(map(str, reversed(sorted(leaders.values())[-5:])))

def main():
    start = time()
    f = open('data/SCC.txt')
    al = f.read()
    f.close()
    al = map(format_stupid_string, al.split('\n'))
    n = 875714 # Assignment tells you the number of nodes.
    m = len(al)

    print kosarajus(al, n)

    end = time()
    print 'program finished in %s seconds' % round(end - start, 2)

if __name__ == '__main__':
    main()