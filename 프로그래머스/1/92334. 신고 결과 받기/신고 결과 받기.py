def solution(id_list, report, k):
    answer = []
    # report_dict: id_list로 dict key 만들기 val = []
    # for 문 돌며 report 에 해당하는 값을 dict key에 append하기
    # reported_dict: key는 id_list for 문 돌며 신고횟수 +=1 하기
    # report_ids: k값보다 높은 신고횟수를 가진 id 검출하기
    # report_dict에서 검출된 report_ids를 가지고 있는지 횟수 더하기
    # answer에 append하기
    
    report_dict = {key:[] for key in id_list}
    for mass in report:
        i,j = mass.split(' ')
        if j not in report_dict[i]:
            report_dict[i].append(j)
    reported_dict = {key:0 for key in id_list}
    for i in report_dict.keys():
        for l in report_dict[i]:
            reported_dict[l]+=1
    report_ids = [idx for idx,count in reported_dict.items() if count>=k]
    for k in report_dict.keys():
        counts = 0
        for l in report_dict[k]:
            if l in report_ids:
                counts+=1
        answer.append(counts)
    return answer