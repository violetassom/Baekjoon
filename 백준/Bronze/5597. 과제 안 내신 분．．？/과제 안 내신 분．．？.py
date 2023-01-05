import sys
submit_list = []
original_list = list(range(1,31))
for i in range(28):
    num = int(sys.stdin.readline())
    submit_list.append(num)
result_list = list(set(original_list)-set(submit_list))
if result_list[0]<result_list[1]:
    min_result = result_list[0]
    max_result = result_list[1]
else:
    min_result = result_list[1]
    max_result = result_list[0]
print(min_result)
print(max_result)