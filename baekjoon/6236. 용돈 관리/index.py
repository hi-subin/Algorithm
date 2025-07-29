import sys
input = sys.stdin.readline

N, M = map(int, input().split())
budget = [int(input()) for _ in range(N)]

max_budget = max(budget)
l, r = min(budget), sum(budget)
K = 0

while l <= r:
    m = (l + r) // 2
    cur_k = m
    cnt = 1

    for cost in budget:
        if cur_k < cost:
            cur_k = m
            cnt += 1
        cur_k -= cost

    if cnt > M or m < max_budget:
        l = m + 1
    else:
        r = m - 1
        K = m

print(K)
