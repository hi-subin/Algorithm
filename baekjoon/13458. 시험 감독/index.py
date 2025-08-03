import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
cnt = 0

for i in range(N):
    cnt += 1
    if A[i] - B > 0:
        cnt += -(-(A[i] - B) // C)

print(cnt)