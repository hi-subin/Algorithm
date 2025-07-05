from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]

def bfs(sx, sy):
    queue = deque()
    queue.append([sx, sy])

    graph[sy][sx] = 0

    while queue:
        cur = queue.popleft()

        for i in range(4):
            x, y = cur[0] + dx[i], cur[1] + dy[i]

            if (0 <= x < M and 0 <= y < N) and graph[y][x] == 1:
                queue.append([x, y])
                graph[y][x] = 0

for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0 for _ in range(M)] for _ in range(N)]
    count = 0
    
    for _ in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1

    for y in range(N):
        for x in range(M):
            if graph[y][x] == 1:
                count += 1
                bfs(x, y)

    print(count)