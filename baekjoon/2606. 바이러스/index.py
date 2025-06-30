import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]
visited = [-1 for _ in range(N + 1)]

for _ in range(M):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

count = 0
def dfs(n):
    global count
    visited[n] = count

    for i in range(len(graph[n])):
        if visited[graph[n][i]] == -1:
            count += 1
            dfs(graph[n][i])
            
dfs(1)

print(count)
