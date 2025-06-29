import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]

for _ in range(M):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

order = 1
def dfs(n):
    global order
    visited[n] = order
    graph[n].sort()
    
    for i in graph[n]:
        if visited[i] == 0:
            order += 1
            dfs(i)

dfs(R)

for _order in visited[1:]:
    print(_order)