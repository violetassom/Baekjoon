n=int(input())
equ = input()
number = []
for _ in range(n):
    number.append(int(input()))
stack = []
for i in equ:
    if i.isalpha():
        which_point=ord(i)-65
        stack.append(number[which_point])
    else:
        b = stack.pop()
        a = stack.pop()
        if i == '+':
            stack.append(a+b)
        elif i == '-':
            stack.append(a-b)
        elif i == '*':
            stack.append(a*b)
        elif i == '/':
            stack.append(a/b)
print(format(stack[0],'.2f'))