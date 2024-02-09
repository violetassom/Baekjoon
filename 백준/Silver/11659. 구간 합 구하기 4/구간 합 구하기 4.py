import sys
n,m = map(int,sys.stdin.readline().split())
num_list = list(map(int,sys.stdin.readline().split()))
cum_list=[]
for i,j in enumerate(num_list):
    if i==0:
        cum_list.append(j)
    else:
        cum_list.append(j+cum_list[-1])
for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    if a==1:
        print(cum_list[b-1])
    else:
        print(cum_list[b-1]-cum_list[a-2])