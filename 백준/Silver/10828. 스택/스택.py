from sys import stdin
n = int(stdin.readline())


#push X: 정수 X를 스택에 넣는 연산이다.
#pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
#size: 스택에 들어있는 정수의 개수를 출력한다.
#empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
#top: 스택의 가장 위에

# push
def go(x,b,stack):
    if x=='push':
        stack.append(b)
        return stack
    if x=='pop':
        if len(stack)==0:
            print(-1)
            return stack
        else:
            print(stack[len(stack)-1])
            stack.pop()
            return stack
    if x=='size':
        print(len(stack))
        return stack
    if x=='empty':
        if len(stack)==0:
            print(1)
            return stack
        else:
            print(0)
            return stack
    if x=='top':
        if len(stack)!=0:
            print(stack[len(stack)-1])
            return stack
        else:
            print(-1)
            return stack
stack = []
for _ in range(n):
    inp = stdin.readline().rstrip().split(' ')
    a=inp[0]
    b=0
    try:
        b=int(inp[1])
    except:
        pass
    stack = go(a,b,stack)
    # print(stack)


# 14
# push 1
# push 2
# top
# size
# empty
# pop
# pop
# pop
# size
# empty
# pop
# push 3
# empty
# top