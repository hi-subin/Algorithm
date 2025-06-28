import sys

n = int(sys.stdin.readline())

for i in range(n):
    stack = []
    flag = False
    command = sys.stdin.readline()

    for j in range(len(command)):
        if command[j] == '(':
            stack.append(command[j])
        elif command[j] == ')':
            if stack:
                stack.pop(-1)
            else:
                print('NO')
                flag = True
                break
    if not flag:
        if stack:
            print('NO')
        else:
            print('YES')