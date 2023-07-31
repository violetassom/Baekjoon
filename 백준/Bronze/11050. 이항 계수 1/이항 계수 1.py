m,n = map(int,input().split())
a=1
b=1
for i in range(m,m-n,-1):
    a *= i
for j in range(1,n+1):
    b *= j
print(int(a/b))