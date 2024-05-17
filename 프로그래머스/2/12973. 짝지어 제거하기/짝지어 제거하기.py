def solution(s):
    # while switch
    # for
    my_stack=[]
    for i in range(len(s)):
        if not my_stack:
            my_stack.append(s[i])
        else:
            if s[i]==my_stack[-1]:
                my_stack.pop()
            else:
                my_stack.append(s[i])

    if not my_stack:
        answer = 1
    else:
        answer = 0

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    # print('Hello Python')

    return answer