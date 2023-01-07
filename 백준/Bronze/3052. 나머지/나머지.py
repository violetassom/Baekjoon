import sys
remainder_list = []
for i in range(10):
    num = int(sys.stdin.readline())
    remainder_list.append(num%42)
result = len(list(set(remainder_list)))
print(result)