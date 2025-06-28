import sys

commandSize = int(sys.stdin.readline())
stack = []

for i in range(commandSize):
    command = sys.stdin.readline().split()
    
    if command[0] == '1':
        stack.append(int(command[-1]))
    elif command[0] == '2':
        if stack:
            print(stack.pop(-1))
        else:
            print(-1)
    elif command[0] == '3':
        print(len(stack))
    elif command[0] == '4':
        if stack:
            print(0)
        else:
            print(1)
    elif command[0] == '5':
        if stack:
            print(stack[-1])
        else:
            print(-1)