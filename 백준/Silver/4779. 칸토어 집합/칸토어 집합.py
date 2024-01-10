# if n=4 3**4
import sys
def cantore(n):
    if n==0:
        return '-'
    else:
        return cantore(n-1)+len(cantore(n-1))*' '+cantore(n-1)
while True:
    try:
        n = int(input())
        print(cantore(n))
    except:
        break