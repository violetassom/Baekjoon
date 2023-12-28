from collections import deque
import sys
n = int(sys.stdin.readline())
stc = deque()


for i in range(n):
    inp = list(map(int, sys.stdin.readline().split()))
    if inp[0] == 1:
        stc.append(inp[1])
    elif inp[0] == 2:
        if stc:
            print(stc.pop())
        else:
            print(-1)
    elif inp[0] == 3:
        print(len(stc))
    elif inp[0] == 4:
        if stc:
            print(0)
        else:
            print(1)
    elif inp[0] == 5:
        if stc:
            print(stc[-1])
        else:
            print(-1)