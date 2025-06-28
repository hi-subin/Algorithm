N, K = list(map(int, input().split()))
coins = [int(input()) for _ in range(N)]
coins.sort(reverse=True)

result = 0
s_i = 0
for i in range(s_i, len(coins) - s_i):
    if K >= coins[i]:
        result += K // coins[i]
        K %= coins[i]
        if K <= 0:
            break

print(result)
