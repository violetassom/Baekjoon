import sys
string = list(input().rstrip())
_dict = {}

for i,j in enumerate(string):
    if j not in _dict.keys():
        _dict[j]=[i]
    else:
        _dict[j].append(i)
        
n = int(input())

for _ in range(n):
    a,b,c = input().split()
    result = 0
    b = int(b)
    c = int(c)
    if a in string:
        for k in _dict[a]:
            if k>=b and k<=c:
                result+=1
    print(result)
    