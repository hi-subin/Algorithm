N = int(input())
meetings = [list(map(int, input().split())) for _ in range(N)]
meetings.sort(key=lambda x: (x[1], x[0]))

curTime = 0
result = 0

for start, end in meetings:
    if curTime <= start:
        result += 1
        curTime = end

print(result)