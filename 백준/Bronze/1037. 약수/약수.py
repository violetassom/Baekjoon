import sys
n = int(sys.stdin.readline())
n_list = list(map(int,sys.stdin.readline().split()))
n_list.sort()
if n==1:
    print(n_list[0]**2)
else:
    print(n_list[0]*n_list[-1])