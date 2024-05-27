
def solution(participant, completion):
    answer = ''
    parti_dict={}
    for i in range(len(participant)):
        if participant[i] not in parti_dict:
            parti_dict[participant[i]] = 1
        else:
            parti_dict[participant[i]] += 1
    for j in range(len(completion)):
        parti_dict[completion[j]]-=1
    for k in parti_dict.keys():
        if parti_dict[k]==1:
            answer=k
    return answer