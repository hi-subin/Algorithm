from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited_dfs = [False for _ in range(N + 1)]
visited_bfs = [False for _ in range(N + 1)]

for _ in range(M):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

def dfs(n):
    print(n, end=' ')
    visited_dfs[n] = True
    graph[n].sort()

    for i in graph[n]:
        if visited_dfs[i] == False:
            dfs(i)

def bfs(n):
    queue = deque()
    queue.append(n)

    visited_bfs[n] = True

    while queue:
        cur = queue.popleft()
        print(cur, end=' ')
        
        graph[cur].sort()
        
        for i in range(len(graph[cur])):
            if visited_bfs[graph[cur][i]] == False:
                queue.append(graph[cur][i])
                visited_bfs[graph[cur][i]] = True

dfs(V)
print()
bfs(V)