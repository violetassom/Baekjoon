total = int(input())
nums = int(input())
real_total = 0
for i in range(nums):
    price, count = map(int, input().split())
    real_total += price * count
if total == real_total:
    print('Yes')
else:
    print('No')