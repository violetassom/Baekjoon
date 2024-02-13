import sys
n,m = map(int,input().split())
num_list = list(map(int,input().split()))
cum_list=[]
for i,j in enumerate(num_list):
    if i==0:
        cum_list.append(j)
    else:
        cum_list.append(j+cum_list[-1])
cum_list2 = []
for k in range(len(cum_list)):
    if k < m-1:
        cum_list2.append(-100*n)
    elif k == m-1:
        cum_list2.append(cum_list[k])
    else:
        cum_list2.append(cum_list[k]-cum_list[k-m])
print(max(cum_list2))