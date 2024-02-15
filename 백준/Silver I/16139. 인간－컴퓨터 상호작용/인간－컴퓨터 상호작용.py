import sys
string = list(sys.stdin.readline().rstrip())
_dict = {}

for i,j in enumerate(string):
    if j not in _dict.keys():
        _dict[j]=[i]
    else:
        _dict[j].append(i)
        
n = int(sys.stdin.readline())

for _ in range(n):
    a,b,c = sys.stdin.readline().split()
    result = 0
    b = int(b)
    c = int(c)
    if a in _dict.keys():
        for k in _dict[a]:
            if k>=b and k<=c:
                result+=1
    print(result)
    