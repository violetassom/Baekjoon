def solution(genres, plays):
    # 장르의 plays 수 총량 구해서 순서정하기
    genre_dict = {}
    index_dict = {}
    for i in range(len(genres)):
        if genres[i] in genre_dict:
            genre_dict[genres[i]]+=plays[i]
            index_dict[genres[i]].append(i)
        else:
            genre_dict[genres[i]]=plays[i]
            index_dict[genres[i]]=[i]
    genre_rank = sorted(genre_dict,key=lambda x:genre_dict[x],reverse=True)
    # 해당 장르의 plays가 높은 2개 꺼내기
    answer = []
    for j in genre_rank:
        one_plays = index_dict[j]
        one_plays_sort = sorted(one_plays,key=lambda x:plays[x],reverse=True)
        if len(one_plays_sort)==1:
            answer.append(one_plays_sort[0])
        else:
            answer.append(one_plays_sort[0])
            answer.append(one_plays_sort[1])
    return answer