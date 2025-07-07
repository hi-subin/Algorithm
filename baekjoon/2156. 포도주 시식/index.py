import sys
input = sys.stdin.readline

n = int(input())
m = [int(input()) for _ in range(n)]
dp = [0] * n

dp[0] = m[0]

if n > 2:
    dp[2] = max(m[0] + m[1], m[1] + m[2], m[0] + m[2])
    dp[1] = m[0] + m[1]
elif n > 1:
    dp[1] = m[0] + m[1]

for i in range(3, n):
    dp[i] = max(dp[i-3] + m[i-1] + m[i], dp[i-2] + m[i], dp[i-1])

print(dp[-1])