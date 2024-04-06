import sys
n = int(sys.stdin.readline())
n_list = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
m_list = list(map(int,sys.stdin.readline().split()))

num_dict = {}
for i in range(n):
    num_dict[n_list[i]]=1

for j in range(m):
    if m_list[j] not in num_dict.keys():
        print(0,end='\n')
    else:
        print(1,end='\n')