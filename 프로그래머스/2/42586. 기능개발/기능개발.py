import math
def solution(progresses, speeds):
    # (100 - progresses)//speeds
    # 7 3 / 12
    # 5 / 10 1 1 / 20 1
    # 맨 앞에가 제일 큰 값이 되어야함. 그 값을 기준으로 더 큰 값이 나오면 그 전에 담은 리스트의 길이를 return 에 넣음
    # days 구하기
    days = []
    num = len(progresses)
    for i in range(num):
        days.append(math.ceil((100-progresses[i])/speeds[i]))
    answer = []
    result = []
    # 반복문 돌면서 stack 맨앞 값이랑 비교했을 때 더 크면 answer에 len 넣기.
    for j in range(num):
        # result 아무것도 없을 때
        if not result:
            result.append(days[j])
        # result 맨 앞값보다 해당값이 클 때
        elif result[0]<days[j]:
            answer.append(len(result))
            result = [days[j]]
        # result 맨 앞값보다 해당값이 작을 때
        elif result[0]>=days[j]:
            result.append(days[j])
    answer.append(len(result))
        
    return answer