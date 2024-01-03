

import sys
n = int(sys.stdin.readline())
empty_li = []
for _ in range(n):
    num = int(sys.stdin.readline())
    empty_li.append(num)
empty_li.sort()
for i in empty_li:
    print(i)