import sys
n,m = map(int,sys.stdin.readline().split())
_dict = {}
for _ in range(n):
    a = sys.stdin.readline().rstrip()
    _dict[a]=0
result = 0
for _ in range(m):
    b = sys.stdin.readline().rstrip()
    if b in _dict:
        result+=1
print(result)