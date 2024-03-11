import sys
n = int(sys.stdin.readline().rstrip())
_dict = {}
count=0
for _ in range(n):
    a = sys.stdin.readline().rstrip()
    if a == "ENTER":
        _dict = {}
    else:
        if a not in _dict.keys():
            _dict[a]=0
            count+=1
print(count)
        