import sys
total_n = int(sys.stdin.readline())
total_list = list(map(int,sys.stdin.readline().split()))
check_n = int(sys.stdin.readline())
check_list = list(map(int,sys.stdin.readline().split()))

_dict = {}
for i in range(total_n):
    if total_list[i] not in _dict.keys():
        _dict[total_list[i]] = 1
    else:
        _dict[total_list[i]] += 1
for j in range(check_n):
    if check_list[j] not in _dict.keys():
        print(0,end=' ')
    else:
        print(_dict[check_list[j]],end=' ')
