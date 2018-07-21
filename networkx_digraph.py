# -*- coding:utf-8 -*-
import networkx as nx
import matplotlib.pyplot as plt

# 创建DAG
G = nx.DiGraph()

# 顶点列表
vertex_list = ['v1', 'v2', 'v3', 'v4', 'v5', 'v6', 'v7']
# 添加顶点
G.add_nodes_from(vertex_list)

# 边列表
edge_list = [
             ('v1', 'v2'), ('v1', 'v3'), ('v1', 'v4'),
             ('v2', 'v4'),('v2', 'v5'),
             ('v3', 'v6'),
             ('v4', 'v3'),('v4', 'v6'),('v4', 'v7'),
             ('v5', 'v4'),('v5', 'v7'),
             ('v7', 'v6')
            ]
# 通过列表形式来添加边
G.add_edges_from(edge_list)

# 指定绘制DAG图时每个顶点的位置
pos = {
        'v1':(-1,1),
        'v2':(1,1),
        'v3':(-2,0),
        'v4':(0,0),
        'v5':(2,0),
        'v6': (-1,-1),
        'v7':(1,-1)
       }
# 绘制DAG图
plt.title('A simple example of DAG')    #图片标题
plt.xlim(-2.2, 2.2)                     #设置X轴坐标范围
plt.ylim(-1.2, 1.2)                     #设置Y轴坐标范围
nx.draw(
        G,
        pos = pos,                 # 点的位置
        node_color = 'red',          # 顶点颜色
        edge_color = 'black',          # 边的颜色
        with_labels = True,        # 显示顶点标签
        font_size =10,             # 文字大小
        node_size =300             # 顶点大小
       )


plt.show()

# DAG的拓扑排序
topological_sort = list(nx.topological_sort(G))
print(topological_sort)