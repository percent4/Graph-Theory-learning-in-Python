from graph import Vertex, Edge, Graph

g = Graph(directed=True)
# 顶点列表
vertex_list = ['a', 'b', 'c', 'd', 'e', 'f']
# 在图中插入顶点
for vertex in vertex_list:
    g.insert_vertex(vertex)

vertices = list(g.vertices())
# 顶点列表中的名称与其在图中对应的点组成一个字典
vertex_dict = {name:vertex for name, vertex in zip(vertex_list, vertices)}
# 从对应顶点连出去的边
edges_map ={
            'a': [('b', 2), ('f', 9)],
            'b': [('c', 1), ('d', 2), ('f', 6)],
            'c': [('d', 7)],
            'd': [('e', 2), ('f', 3)],
            'e': [('f', 4)],
            'f': []
            }

# 在图中插入边
for vertex in vertices:
    for connect_vertex in edges_map[vertex.element()]:
        g.insert_edge(vertex_dict[vertex.element()], vertex_dict[connect_vertex[0]], connect_vertex[1])

# 输出图中所有的边
print('一共有%d个顶点，一共有%d条边。'%(g.vertex_count(), g.edge_count()))
print('图中所有的边为:')
for edge in g.edges():
    start, end = edge.endpoints()
    weight = edge.element()
    print('%s->%s, weight: %s'%(start.element(), end.element(), weight))


# topological order of DAG
# parameter: g -> Graph class
# return: topological order of DAG in list format
def topological_sort(g):
    # Return a list of vertices of DAG g in topological order
    # if graph g has a cycle, the result will be incomplete

    topo = []               # a list of vertices placed in topological order
    ready = []              # list of vertices that have no remaining constraints
    incount = {}            # keep track of in-degree for each vertex
    for u in g.vertices():
        incount[u] = g.degree(u, False)    # parameter requests incoming degree
        if incount[u] == 0:                # if u has no incoming edges
            ready.append(u)                # it is free of constaints

    while len(ready) > 0:
        u = ready.pop()                    # u is free of constraints
        topo.append(u)                     # add u to the topological order
        for e in g.incident_edges(u):      # consider all outgoing neighbors of u
            v = e.opposite(u)
            incount[v] -= 1                # v has one less constaints without u
            if incount[v] == 0:
                ready.append(v)

    return topo

topo = topological_sort(g)
topological_order = [vertex.element() for vertex in topo]
print('该图的拓扑序列为 %s.'%topological_order)

# W: 邻接表(带权值), s: 起始点, t: 终止点
# 求解DAG上的最短路径(shortest-path)
def dag_sp(g, edges_map, s, t):
    # 初始化
    d = {u:float('inf') for u in edges_map.keys()}
    d[s] = 0
    path = [t]
    # DP算法求解最短路径'
    # 先对图进行拓扑排序
    topological_order = [_.element() for _ in topological_sort(g)]
    for u in topological_order:
        if u == t:
            break
        for vertex, weight in edges_map[u]:
            d[vertex] = min(d[vertex], d[u] + weight)
    # print(d)

    # 寻找最佳路径
    part_graph = topological_order[0:topological_order.index(t)]
    part_graph.reverse()
    target = t
    for vertex in part_graph:
        if g.get_edge(vertex_dict[vertex], vertex_dict[target]) is not None:
            if d[vertex] + g.get_edge(vertex_dict[vertex], vertex_dict[target]).element() == d[target]:
                path.append(vertex)
                target = vertex
    #print(path)
    path.reverse()

    return d[t], path

sp_length, path = dag_sp(g=g, edges_map=edges_map, s='a', t='f')
print('最短路径为：%s, 其长度为：%s'%(path, sp_length))