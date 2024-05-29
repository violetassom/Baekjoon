def solution(enroll, referral, seller, amount):
    # parent_dict = {} 자신의 부모노드를 뜻하는 dict를 구하기
    # total_dict = {} 각 enroll에 해당하는 amount 값 0으로 넣기
    # for range len seller 돌면서 해당 amount*100의 0.9 값을 total_dict에 넣고
    # while 문을 돌면서 parent_dict가 0이 나올 때까지 혹은 profit이 0이 될때까지
    # left_profit을 parent_dict에 0.1에 해당하는 값에 parent 유무따라 추가한다
    
    parent_dict = {key:val for key,val in zip(enroll,referral)}
    total_dict = {key:0 for key in enroll}
    for i in range(len(seller)):
        total_dict[seller[i]] += (amount[i]*100)*0.9
        left_profit = (amount[i]*100)*0.1
        seller_son = seller[i]
        seller_parent = parent_dict[seller_son]
        while True:
            # parent가 -인 경우 stop and 마지막 profit 더하기
            if seller_parent=='-':
                break
            # parent가 있는 경우
            else:
                # left profit이 10 미만일 때는 남은 금액 다 더하기
                if left_profit//10==0:
                    total_dict[seller_parent]+=left_profit
                    break
                # 그외 케이스 left profit 0.9먹고 0.1은 부모몫으로 남겨두기
                else:
                    total_dict[seller_parent]+=(left_profit-int(left_profit*0.1))
                    left_profit = int(left_profit*0.1)
                    seller_son = seller_parent
                    seller_parent = parent_dict[seller_son]
    answer = list(map(int,total_dict.values()))
    return answer
