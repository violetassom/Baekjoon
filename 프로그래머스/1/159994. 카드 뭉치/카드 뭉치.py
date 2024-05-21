def solution(cards1, cards2, goal):
    answer = ''
    # for 반복문 goal의 길이만큼
    for i in range(len(goal)):
        # cards1이랑 cards2의 맨앞에 있는 값을 goal 맨앞과 비교
        if cards1 and cards1[0]==goal[0]:
            cards1.pop(0)
            goal.pop(0)
        elif cards2 and cards2[0]==goal[0]:
            cards2.pop(0)
            goal.pop(0)
    # print(goal)
        # 맞다면 둘다 pop(0)
    # goal 비어있으면 Yes 아니면 No
    if not goal:
        answer = 'Yes'
    else:
        answer = 'No'
    return answer