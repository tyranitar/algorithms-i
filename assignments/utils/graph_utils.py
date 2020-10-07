from sets import Set

def add_unit_directed(g, node_a, node_b):
    if node_a not in g:
        g[node_a] = []

    g[node_a].append(node_b)

def add_unit_directed_reverse(g, node_a, node_b):
    add_unit_directed(g, node_b, node_a)

def construct_unit_graph(al, add_to_graph = add_unit_directed):
    g = {}

    for edge in al:
        node_a = edge[0]
        node_b = edge[1]

        add_to_graph(g, node_a, node_b)

    return g

# Imported from graph_utils in algorithms_ii; keep synced.

def add_directed(graph, node_a, node_b, edge_len):
    if node_a not in graph:
        graph[node_a] = {}

    graph[node_a][node_b] = edge_len

def add_directed_reverse(graph, node_a, node_b, edge_len):
    add_directed(graph, node_b, node_a, edge_len)

def add_undirected(graph, node_a, node_b, edge_len):
    add_directed(graph, node_a, node_b, edge_len)
    add_directed_reverse(graph, node_a, node_b, edge_len)

def format_adjacency_list(adjacency_list):
    return map(lambda x: tuple(map(int, x.split(' '))), adjacency_list)

def construct_graph(adjacency_list, add_to_graph = add_undirected):
    adjacency_list = format_adjacency_list(adjacency_list)

    graph = {}

    al_len = len(adjacency_list)

    for i in range(al_len):
        adjacency = adjacency_list[i]
        node_a = adjacency[0]
        node_b = adjacency[1]
        edge_len = adjacency[2]

        add_to_graph(graph, node_a, node_b, edge_len)

    return graph

# End of imported methods.

# Iterative implementation of DFS.
# g = graph
# s = source
# e = explored set
# cb = callback
def dfs(g, s, e, cb):
    stack = [s]

    while stack:
        u = stack.pop()

        if type(u) is str: # u has completely emerged from dfs.
            cb(int(u))
        elif u not in e: # u yet to be explored.
            e.add(u)
            stack.append(str(u)) # bookkeeping end of u's dfs.

            if u in g:
                stack.extend(g[u])