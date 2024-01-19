import sys
n = int(sys.stdin.readline())
coordinate_dict = {}
for _ in range(n):
    x,y = map(int,sys.stdin.readline().split())
    if y not in coordinate_dict.keys():
        coordinate_dict[y]=[x]
    else:
        coordinate_dict[y].append(x)
y_list = list(coordinate_dict.keys())
y_list.sort()
for i in y_list:
    x_list = coordinate_dict[i]
    x_list.sort()
    for j in x_list:
        print(j,i)