import sys
input = sys.stdin.readline

N = int(input())
m = [list(map(int, input().split())) for _ in range(N)]
m.sort()
dp = [1] * N

for i in range(1, N):
    for j in range(0, i):
        if m[j][1] < m[i][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))
