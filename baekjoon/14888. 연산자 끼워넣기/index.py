import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
add, subtract, multiply, divide = map(int, input().split())

max_res = float('-inf')
min_res = float('inf')

def backtrack(idx, res, add, subtract, multiply, divide):
    global max_res, min_res

    if idx == N:
        max_res = max(max_res, res)
        min_res = min(min_res, res)
        return

    if add > 0:
        backtrack(idx + 1, res + nums[idx], add - 1, subtract, multiply, divide)
    if subtract > 0:
        backtrack(idx + 1, res - nums[idx], add, subtract - 1, multiply, divide)
    if multiply > 0:
        backtrack(idx + 1, res * nums[idx], add, subtract, multiply - 1, divide)
    if divide > 0:
        if res < 0:
            backtrack(idx + 1, -(-res // nums[idx]), add, subtract, multiply, divide - 1)
        else:
            backtrack(idx + 1, res // nums[idx], add, subtract, multiply, divide - 1)

backtrack(1, nums[0], add, subtract, multiply, divide)

print(max_res)
print(min_res)
