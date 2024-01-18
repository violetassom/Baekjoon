import sys
n = int(sys.stdin.readline())
coordinate_dict = {}
for _ in range(n):
    a,b = map(int,sys.stdin.readline().split())
    if a not in coordinate_dict.keys():
        coordinate_dict[a] = [b]
    else:
        coordinate_dict[a].append(b)
x_list = list(coordinate_dict.keys())
x_list.sort()
for i in x_list:
    y_list = coordinate_dict[i]
    y_list.sort()
    for j in y_list:
        print(i,j,end="\n")