import sys
input = sys.stdin.readline

n = int(input())
m = list(map(int, input().split()))
m.sort()

size = 0
for i in range(0, n):
    target = m[i]

    l = 0
    r = n - 1

    while l < r:
        if m[l] + m[r] == target:
            if l == i:
                l += 1
            elif r == i:
                r -= 1
            else:
                size += 1
                break
        elif m[l] + m[r] > target:
            r -= 1
        elif m[l] + m[r] < target:
            l += 1
    
print(size)
