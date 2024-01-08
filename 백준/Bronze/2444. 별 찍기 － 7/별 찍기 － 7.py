# import sys
# n = int(sys.stdin.readline())
n=int(input())
max_n = 2*n-1
for i in range(1,n+1):
    print(' '*int((max_n-(2*i-1))/2)+'*'*(2*i-1))
for j in range(n-1,-1,-1):
    print(' '*int((max_n-(2*j-1))/2)+'*'*(2*j-1))
    