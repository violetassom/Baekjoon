import sys
from collections import deque
n,k = map(int,sys.stdin.readline().split())
queue = deque(range(1,n+1))
result = []
for _ in range(n):
    for _ in range(k):
        queue.append(queue.popleft())
    result.append(queue.pop())
print('<'+', '.join(map(str,result))+'>')