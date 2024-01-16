import sys
n = list(map(int,input()))
n.sort()
n.reverse()
print(*n,sep="")