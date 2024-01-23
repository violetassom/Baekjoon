from collections import deque
import sys
n = int(sys.stdin.readline())
li = deque(range(1,n+1))
for i in range(n):
    if i!=n-1:
        li.popleft()
        li.append(li.popleft())
print(li[0])