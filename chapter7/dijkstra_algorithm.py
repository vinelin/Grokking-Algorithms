def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


graph = {'start': {'a': 6, 'b': 2}, 'a': {'fin': 1}, 'b': {'a': 3, 'fin': 5}, 'fin': {}}
infinity = float('inf')
costs = {'a': 6, 'b': 2, 'fin': infinity}
parents = {'a': 'start', 'b': 'start', 'fin': None}
processed = []
node = find_lowest_cost_node(costs) # 在未处理的节点中找出最小开销的节点
while node is not None:  # 这个while循环在所有节点被处理后结束
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys(): # 遍历当前节点的所有邻居
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:  # 如果当前节点前往该邻居更近
            costs[n] = new_cost  # 更新该节点的开销
            parents[n] = node   # 同时设置该邻居的父节点为当前节点
    processed.append(node)  # 标记该节点为处理过
    node = find_lowest_cost_node(costs)  # 处理接下来的节点


print(costs, parents)