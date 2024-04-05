import sys

n, m = map(int, sys.stdin.readline().split())

ear_list = []
see_list = []
for i in range(n + m):
    temp = sys.stdin.readline().rstrip()
    if i<=n-1:
        ear_list.append(temp)
    elif i>=n and i<=n+m-1:
        see_list.append(temp)    

result = list(set(ear_list)&set(see_list))
result.sort()
print(len(result))
print(*result,sep="\n")