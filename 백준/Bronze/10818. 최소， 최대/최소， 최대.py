import sys

counts = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().rstrip().split()))
# max_result=0
# min_result=0
# for i in range(len(numbers)):
#     if i == 0:
#         max_result = numbers[i]
#     else:
#         if i > max_result:
#             max_result = i
# for j in range(len(numbers)):
#     if j == 0:
#         min_result = numbers[j]
#     else:
#         if numbers[j] < min_result:
#             min_result = numbers[j]


min_result = min(numbers)
max_result = max(numbers)
print(min_result, max_result)
