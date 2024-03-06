import sys
n = int(sys.stdin.readline())
state_dict = {}
for _ in range(n):
    name, state = sys.stdin.readline().split()
    if name not in state_dict.keys():
        if state=="enter":
            state_dict[name]=1
    else:
        if state == "leave":
            state_dict[name]=0
        else:
            state_dict[name]=1
result = []
for i,j in state_dict.items():
    if j==1:
        result.append(i)
result.sort(reverse=True)
print(*result,sep="\n")  
# print(state_dict)