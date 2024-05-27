from collections import deque
def solution(want, number, discount):
    answer = 0
    # want_dict: want - number dict 만들기
    # discount_dict: 첫 9 dict 만들기
    # deq_dis: discount deque 형식
    
    # for i in range(9,len(discount)-1)
    #   if i in discount_dict:
    #       discount_dict[i] += 1
    #   else:
    #       discount_dict[i] = 1
    #   check=0
    #   for want key
    #       if key=dict[key] 맞는다면
    #           check+=1
    #   if check==len(want.keys()):
        # answer +=1
    #   discount_dict[deq_dis.popleft()] -= 1
    
    
    # want_dict: want - number dict 만들기
    want_dict = {}
    for i in range(len(want)):
        want_dict[want[i]]=number[i]
    # discount_dict: 첫 9 dict 만들기
    discount_dict = {}
    for j in range(9):
        if discount[j] in discount_dict:
            discount_dict[discount[j]]+=1
        else:
            discount_dict[discount[j]]=1
    # print(want_dict)
    # print(discount_dict)
    # deq_dis: discount deque 형식
    deq_dis = deque(discount)
    # print(deq_dis)
    # for i in range(9,len(discount)-1)
    # print(range(9,len(discount)-10))
    for k in range(9,len(discount)):
        if discount[k] in discount_dict:
            discount_dict[discount[k]] += 1
        else:
            discount_dict[discount[k]] = 1
        # print(discount_dict)
        check = 0
        for l in want_dict.keys():
            if l in discount_dict:
                if want_dict[l]==discount_dict[l]:
                    check+=1
        if check == len(want_dict.keys()):
            answer += 1
        discount_dict[deq_dis.popleft()]-=1
    return answer