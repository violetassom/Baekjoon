import sys
n,a = map(int,sys.stdin.readline().split())
measure_list = []
for i in range(1,n//2+1):
    if i==1:
        measure_list.append(1)
        measure_list.append(n)
    elif n%i==0:
        measure_list.append(i)
        measure_list.append(n//i)

final_list = list(set(measure_list))
final_list.sort()
try:
    print(final_list[a-1])
except:
    print(0)