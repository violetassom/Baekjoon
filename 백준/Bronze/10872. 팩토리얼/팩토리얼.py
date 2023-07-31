n = int(input())
result = 1
for i in range(1,n+1):
    if (i==0) or (i==1):
        result*=1
    else:
        result*=i
print(result)