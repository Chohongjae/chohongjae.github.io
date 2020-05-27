from collections import deque


def bfs(graph, start):
    queue = deque([start])
    visited = []
    while queue:
        current = queue.popleft()
        if current not in visited:
            visited.append(current)
            if current in graph:
                tmp = list(set(graph[current]) - set(visited))
                tmp.sort()
                queue += tmp

    return ' '.join([str(i) for i in visited])


def dfs(graph, start):
    stack = [start]
    visited = []
    while stack:
        current = stack.pop()
        if current not in visited:
            visited.append(current)
            if current in graph:
                tmp = list(set(graph[current]) - set(visited))
                tmp.sort(reverse=True)
                stack += tmp

    return ' '.join([str(i) for i in visited])



graph = {}
n = input().split(' ')
node, edge, start = [int(i) for i in n]
for i in range(edge):
    edge_info = input().split(' ')
    n1, n2 = [int(j) for j in edge_info]
    if n1 not in graph:
        graph[n1] = [n2]
    elif n2 not in graph[n1]:
        graph[n1].append(n2)

    if n2 not in graph:
        graph[n2] = [n1]
    elif n1 not in graph[n2]:
        graph[n2].append(n1)

print(dfs(graph, start))
print(bfs(graph, start))


    #
    # n, m, v = map(int, input().split())
    # graph = {}
    # for i in range(m):
    #     t = input().split()
    #     if t[0] not in graph:
    #         graph[t[0]] = [t[1]]
    #     else:
    #         graph[t[0]].append(t[1])
    #
    #     if t[1] not in graph:
    #         graph[t[1]] = [t[0]]
    #     else:
    #         graph[t[1]].append(t[0])
