n,b = map(int,input().split())
stack = []
# 60466175 36

while True:
    top = n//b
    if top == 0:
        stack.append(n%b)
        break
    else:
        stack.append(n%b)
        n = n//b
stack.reverse()
for i in stack:
    if i >= 10:
        print(chr(i+55),end='')
    else:
        print(i,end='')