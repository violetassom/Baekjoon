def solution(phone_book):
    # 길이대로 dict 만들기
    len_dict = {}
    # for i 
    for i in range(len(phone_book)):
        if len(phone_book[i]) not in len_dict:
            len_dict[len(phone_book[i])]=[phone_book[i]]
        else:
            len_dict[len(phone_book[i])].append(phone_book[i])
    # dict key 값만큼 잘랐을 때의 set값이 자르기 전과 같다면 true, 다르다면 false
    # for j 
    for j in len_dict.keys():
        # 해당 키가 아닌 값들 구하기
        cut_words = [word[:j] for word in phone_book if len(word)>j]
        # 해당 키가 아닌 값들 set로 구하기
        set_cut_words = set(cut_words)
        # set_cut_words.add(len_dict[j])
        # set로 intersection있으면 false
        if set_cut_words.intersection(len_dict[j]):
            return False
    answer = True
    return answer