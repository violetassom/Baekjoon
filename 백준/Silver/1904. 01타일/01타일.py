import sys
n = int(sys.stdin.readline())
result=[1,1,2]
for i in range(3,n+1):
    result.append((result[i-1]+result[i-2])%15746)
if n==1:
    print(result[n])    
else:
    print(result[-1])