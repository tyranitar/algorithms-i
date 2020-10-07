from sys import path
path.append('../utils')

from dijkstras import dijkstras
from graph_utils import construct_graph

inf = float('inf')

def parse_inf(x):
    global inf

    if x == inf:
        return 1000000
    return x

def main():
    vertices = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
    s = 1
    n = 200

    f = open('data/dijkstraData.txt')
    a = []

    for line in f:
        line = line.rstrip()
        if line:
            a.append(line)

    f.close()

    al = []

    for row in a:
        r = row.split('\t')
        u = r[0]
        r = r[1:]

        for v_e in r:
            al.append(' '.join([u] + v_e.split(',')))

    g = construct_graph(al)
    A = dijkstras(g, s, n)

    vertices = map(lambda x: str(parse_inf(A[x])), vertices)
    print ','.join(vertices)

if __name__ == '__main__':
    main()