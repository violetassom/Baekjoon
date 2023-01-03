import sys
counts = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().rstrip().split()))
find_num = int(sys.stdin.readline())
#input_list = []
result = 0
for i in nums:
    if i == find_num:
        result+=1
print(result)