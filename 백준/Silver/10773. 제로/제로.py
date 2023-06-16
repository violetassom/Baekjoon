n=int(input())
li = []
for _ in range(n):
    x = int(input())
    if x!=0:
        li.append(x)
    else:
        li.pop()
print(sum(li))