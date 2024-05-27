def solution(record):
    answer = []
    # for uid dict로 이름 최종 결정하기
    id_dict = {}
    for k in record:
        i=k.split(' ')
        if i[0]!='Leave':
            id_dict[i[1]]=i[2]
    # result는 uid dict val 값으로 대체하
    for l in record:
        j=l.split(' ')
        if j[0] != "Change":
            if j[0] == "Enter":
                string = f'{id_dict[j[1]]}님이 들어왔습니다.'
            else:
                string = f'{id_dict[j[1]]}님이 나갔습니다.'
            # print(string)
            answer.append(string)
    # for 문으로 최종 result 담기
    
    
    return answer