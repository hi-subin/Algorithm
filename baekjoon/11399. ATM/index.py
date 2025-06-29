N = int(input())
time = list(map(int, input().split()))
time.sort()

cumsum = 0
result = 0
for i in range(N):
    cumsum += time[i]
    result += cumsum

print(result)