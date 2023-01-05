import sys

length = 9
total_list = []
for i in range(length):
    num = int(sys.stdin.readline())
    total_list.append(num)
max_num = max(total_list)
max_index = total_list.index(max_num)
print(max_num)
print(max_index+1)