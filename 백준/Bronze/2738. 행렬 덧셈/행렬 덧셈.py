n, m = map(int, input().split())
m1 = []
m2 = []
for i in range(n):
    m1.append(list(map(int, input().split())))
for i in range(n):
    m2.append(list(map(int, input().split())))
result = m1 + m2
# breakpoint()
for x,y in zip(m1,m2):
    for i in range(m):
        print(x[i]+y[i],end=' ')
    print()
    # for i in x:
    #     for j in y:
    #         print(i+j,end=' ')