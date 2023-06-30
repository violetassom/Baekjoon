import sys
slice_stack = []
stack = []
stick = sys.stdin.readline().rstrip()
switch=0
for i in stick:
    if i == '(':
        if switch == 0:
            switch=1
        else:
            slice_stack.append(1)

    else:
        if switch==1:
            switch=0
            slice_stack = [j+1 for j in slice_stack]
            # for j in range(len(slice_stack)):
            #     slice_stack[j] = slice_stack[j]+1
        else:
            stack.append(slice_stack.pop())
print(sum(stack))
# ()(((()())(())()))(())