import sys
n = int(sys.stdin.readline())
age_dict = {}
for _ in range(n):
    num,name = sys.stdin.readline().split()
    num = int(num)
    if num not in age_dict.keys():
        age_dict[num]=[name]
    else:
        age_dict[num].append(name)
age_list = list(age_dict.keys())
age_list.sort()
for i in age_list:
    for j in age_dict[i]:
        print(i,j)