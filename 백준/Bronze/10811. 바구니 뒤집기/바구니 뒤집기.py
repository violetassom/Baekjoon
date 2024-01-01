#5 4
#1 2
#3 4
#1 4
#2 2
#12345
#21345
#21435
#34125
#34125
# 3 4 1 2 5
import sys
basket_num, n = map(int, sys.stdin.readline().split())

basket = list(range(1,basket_num+1))
for _ in range(n):
    a,b = map(int, sys.stdin.readline().split())
    if a==b:
        pass
    else:
        sample_li = basket[a-1:b][::-1]
        basket[a-1:b]= sample_li
for i in basket:
    print(i,end=" ")