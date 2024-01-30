import sys
from collections import deque
n = int(sys.stdin.readline())
li = deque()
for _ in range(n):
    deck = list(map(int,sys.stdin.readline().split()))
    if deck[0]==1:
        li.appendleft(deck[1])
    elif deck[0]==2:
        li.append(deck[1])
    elif deck[0]==3:
        if len(li)!=0:
            print(li.popleft())
        else:
            print(-1)
    elif deck[0]==4:
        if len(li)!=0:
            print(li.pop())
        else:
            print(-1)
    elif deck[0]==5:
        print(len(li))
    elif deck[0]==6:
        if len(li)!=0:
            print(0)
        else:
            print(1)
    elif deck[0]==7:
        if len(li)!=0:
            print(li[0])
        else:
            print(-1)
    elif deck[0]==8:
        if len(li)!=0:
            print(li[-1])
        else:
            print(-1)
    