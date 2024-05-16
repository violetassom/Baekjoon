def solution(answers):
    # answer pattern
    a1 = [1,2,3,4,5]
    a2 = [2, 1, 2, 3, 2, 4, 2, 5]
    a3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    result = [0,0,0]
    # a1의 경우
    for j in range(len(answers)):
        if a1[j%len(a1)]==answers[j]:
            result[0]+=1
    # a2의 경우
    for j in range(len(answers)):
        if a2[j%len(a2)]==answers[j]:
            result[1]+=1
    # a3의 경우
    for j in range(len(answers)):
        if a3[j%len(a3)]==answers[j]:
            result[2]+=1
    
    # 비교하기
    answer = []
    if result[0]>= result[1] and result[0]>=result[2]:
        answer.append(1)
    if result[1]>= result[0] and result[1]>=result[2]:
        answer.append(2)
    if result[2]>= result[0] and result[2]>=result[1]:
        answer.append(3)      

    return answer