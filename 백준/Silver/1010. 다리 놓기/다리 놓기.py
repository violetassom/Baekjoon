import sys
from math import comb

n = int(input())
for _ in range(n):
    N,M = map(int,input().split())
    result = comb(M,N)
    print(result)