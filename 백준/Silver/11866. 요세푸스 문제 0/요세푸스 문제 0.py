from collections import deque
import sys
n,k = map(int,sys.stdin.readline().split())
deq = deque(range(1,n+1))
result = deque()
while True:
    if len(deq)==1:
        result.append(deq.popleft())
        break
    else:
        for i in range(k):
            if i==k-1:
                result.append(deq.popleft())
            else:
                deq.append(deq.popleft())
        #     print('cnt',cnt)    
        #     print('num',num)
        #     print('deq',deq)
        #     print('result',result)
        # break
# print(*result,sep=', ')
print("<",end="")
for j in range(len(result)):
    if j!=len(result)-1:
        print(result[j],end=", ")
    else:    
        print(result[j],end="")
print(">")
