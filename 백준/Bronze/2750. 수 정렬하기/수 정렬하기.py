
count = int(input())
result_list = []
for i in range(count):
    num = int(input())
    result_list.append(num)
result_list.sort()
for j in result_list:
    print(j)