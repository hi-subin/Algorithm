import sys
input = sys.stdin.readline

A = int(input())
m = list(map(int, input().split()))
dp = [1] * A

for i in range(1, A):
    for j in range(i):
        if m[i] > m[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
