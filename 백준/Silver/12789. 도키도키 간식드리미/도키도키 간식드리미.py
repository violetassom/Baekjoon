import sys
n = input()
line_li = map(int,input().split())

li = []
input_n = 1

for i in line_li:
    if i!=input_n:
        if len(li)!=0:
            if li[-1]==input_n:
                for _ in range(len(li)):
                    if li[-1]==input_n:
                        li.pop()
                        input_n+=1
                if i==input_n:
                    input_n+=1
                else:
                    li.append(i)
            else:
                li.append(i)
        else:
            li.append(i)
    else:
        input_n+=1

for _ in range(len(li)):
    if li[-1]==input_n:
        li.pop()
        input_n+=1

if len(li)==0:
    print('Nice')
else:
    print('Sad')