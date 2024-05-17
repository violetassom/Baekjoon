def is_it_right(s):
    # couple dict
    couple_dict = {']':'[',')':'(','}':'{'}
    len_s = len(s)
    my_stack = []
    for i in range(len_s):
        if i == 0:
            for j in s:
                if (j=='(') or (j=='[') or (j=='{'):
                    my_stack.append(j)
                else:
                    if not my_stack:
                        my_stack.append(j)
                        break
                    else:
                        if my_stack[-1]==couple_dict[j]:
                            my_stack.pop()
                        else:
                            my_stack.append(j)
    # print(my_stack)
    if not my_stack:
        return 1
    else:
        return 0
def solution(s):
    # len 구하기
    len_s = len(s)
    answer = 0
    s = list(s)
    
    # for 문으로 회전한 모형 구하기
    # 구한 모형이 맞는지 확인하기
    # 맞다면 answer +=1
    for i in range(len_s):
        my_stack = []
        if i == 0:
            answer += is_it_right(s)
            # print(s,is_it_right(s))
        else:
            pop_string = s.pop(0)
            s.append(pop_string)
            # print(s,is_it_right(s))
            answer += is_it_right(s)
                    
    return answer