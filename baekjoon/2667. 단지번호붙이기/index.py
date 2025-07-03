import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
grid = [list(map(int, input().strip())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]
result = []
count = 0

def dfs(sx, sy):
    global count
    count += 1
    visited[sy][sx] = True
    
    for i in range(4):
        x, y = sx + dx[i], sy + dy[i]
        
        if (0 <= x < N and 0 <= y < N) and not visited[y][x] and grid[y][x] == 1:
            dfs(x, y)

for i in range(N):
    for j in range(N):
        if not visited[j][i] and grid[j][i] == 1:
            count = 0
            dfs(i, j)
            result.append(count)
            
print(len(result), end='\n')
result.sort()
for i in result:
    print(i)

