from collections import deque
import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [0 for _ in range(N + 1)]

for _ in range(M):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

order = 1
def bfs(n):
    global order
    queue = deque()
    queue.append(n)

    visited[n] = order

    while queue:
        cur = queue.popleft()
        graph[cur].sort(reverse=True)
        
        for i in range(len(graph[cur])):
            if visited[graph[cur][i]] == 0:
                queue.append(graph[cur][i])
                order += 1
                visited[graph[cur][i]] = order

bfs(R)

for i in visited[1:]:
    print(i)