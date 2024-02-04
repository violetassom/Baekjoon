import sys
n = int(sys.stdin.readline())
len_dict = {}
for _ in range(n):
    a = sys.stdin.readline().rstrip()
    num = len(a)
    if num not in len_dict.keys():
        len_dict[num] = [a]
    else:
        len_dict[num].append(a)
len_list = list(len_dict.keys())
len_list.sort()
for i in len_list:
    spe_len_list = list(set(len_dict[i]))
    spe_len_list.sort()
    for j in spe_len_list:
        print(j,end="\n")