from copy import deepcopy
from math import log
from random import choice
from sets import Set

def construct_graph(a):
    g = {}

    for vertices in a:
        u = vertices[0]

        for i in range(1, len(vertices)):
            v = vertices[i]

            if u not in g:
                g[u] = {}

            if v not in g:
                g[v] = {}

            g[u][v] = 1
            g[v][u] = 1

    return g

def karger_min_cut(g):
    n = len(g.keys())

    while n > 2:
        u = choice(g.keys())
        v = choice(g[u].keys())

        for key in g[v]:
            if key != u:
                if u not in g[key]:
                    g[key][u] = 0
                    g[u][key] = 0

                g[key][u] += g[key][v]
                g[u][key] += g[key][v]

            del g[key][v]

        del g[v]

        n -= 1

    return g.itervalues().next().itervalues().next()

def repeat_karger_min_cut(a):
    n = len(a)
    num_repeats = int(round(pow(n, 2) * log(n)))
    # num_repeats = 10000
    min_cut = float('inf')

    for i in range(num_repeats):
        print round((float(i) / num_repeats) * 100, 2)
        new_min_cut = karger_min_cut(construct_graph(a))

        if new_min_cut < min_cut:
            min_cut = new_min_cut

    return min_cut


def main():
    f = open('data/_f370cd8b4d3482c940e4a57f489a200b_kargerMinCut.txt')
    # f = open('data/custom.txt')
    a = f.readlines()
    f.close()
    a = map(lambda x: map(int, x.split('\t')[:-1]), a)
    # a = map(lambda x: map(int, x.split(' ')[:-1]), a)
    print repeat_karger_min_cut(a)

if __name__ == '__main__':
    main()