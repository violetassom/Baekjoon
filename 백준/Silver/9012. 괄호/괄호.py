n = int(input())
def bool_vps(x):
    li = []
    for i in range(len(x)):
        if i==0:
                if x[i]=='(':
                    li.append(x[i])
                else:
                    li.append(x[i])
                    break
        else:
            # li가 비어있다면
            if len(li)==0:
                if x[i]=='(':
                    li.append(x[i])
                else:
                    li.append(x[i])
                    break
            # li 맨 끝에 들어있는 값이 들어갈 값과 같다면 넣기
            elif li[len(li)-1]==x[i]:
                li.append(x[i])
            # 같지 않다면 li에서 뺴기
            else:
                li.pop()
    # li가 비어있다면 YES
    if len(li)==0:
        print('YES')
    else:
        print('NO')

for _ in range(n):
    input_x = input()
    bool_vps(input_x)