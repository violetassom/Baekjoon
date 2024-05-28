import itertools
def solution(orders, course):
    # comb_dict = {}
    # for i orders
        # for j course
            # comb_dict
    # sorted
    answer=[]
    comb_dict = {}
    for j in course:
        for i in orders:
            i = sorted(list(i))
            comb_result = itertools.combinations(i,j)
            for k in comb_result:
                if k not in comb_dict:
                    comb_dict[k]=1
                else:
                    comb_dict[k]+=1
    for j in course:
        temp_comb_dict = {''.join(key):val for key,val in comb_dict.items() if len(key)==j}
        if len(temp_comb_dict)!=0:
            max_dict = max(temp_comb_dict.values())
            if max_dict>1:
                temp_comb_dict = {key:val for key,val in temp_comb_dict.items() if val==max_dict}
                result = sorted(temp_comb_dict,key=lambda x: temp_comb_dict[x],reverse=True)
                answer.extend(result)

    answer.sort()
    return answer