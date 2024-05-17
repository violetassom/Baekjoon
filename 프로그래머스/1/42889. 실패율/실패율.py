def solution(N, stages):
    # 1) stages dict화
    stage_dict = {}
    for i in range(1,N+2):
        stage_dict[i]=0
    for j in stages:
        stage_dict[j]+=1
    # print(stage_dict)
    
    # 2) for 문으로 +1과 분모 구하기
    fail_rate = {}
    denom = len(stages)
    for k in range(1,N+1):
        if stage_dict[k]==0:
            fail_rate[k]=0
        else:
            fail_rate[k]=stage_dict[k]/denom
            denom -= stage_dict[k]
    
    # 3) 실패율 정렬
    # 실패율 내림차순
    # 실패율 --- 스테이지 레벨
#     fail_dict = {}
#     for idx,rate in enumerate(fail_rate):
#         fail_dict[idx+1]=rate
#     # print(fail_rate)
#     keys = list(fail_dict.keys())
#     vals = list(fail_dict.values())
    # rank_fail = [sorted(fail_rate,reverse=True).index(m)+1 for m in fail_rate]
    # rank_fail2 = [sorted(rank_fail,reverse=True).index(n)+1 for n in rank_fail]
    # rank_fail3 = [fail_rate.index(o)+1 for o in sorted(fail_rate,reverse=True)]
    # print(rank_fail)
    # print(rank_fail2)
    # print(rank_fail3)
    
    # answer = []
    answer = sorted(fail_rate,key=lambda x: fail_rate[x],reverse=True)
    return answer