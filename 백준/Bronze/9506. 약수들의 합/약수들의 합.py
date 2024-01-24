import sys
while True:
    n = int(input())
    if n==-1:
        break
    else:
        measure_list = []
        for i in range(1,n//2+1):
            if i==1:
                measure_list.append(1)
            elif n%i==0:
                measure_list.append(i)
                measure_list.append(n//i)

        final_list = list(set(measure_list))
        final_list.sort()
        if sum(final_list)==n:
            print(n,'=',end=" ")
            print(*final_list,sep=" + ")
        else:
            print(n,"is NOT perfect.")