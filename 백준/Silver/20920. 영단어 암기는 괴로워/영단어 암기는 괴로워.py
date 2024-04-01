#자주 나오는 단어일수록 앞에 배치한다.
#해당 단어의 길이가 길수록 앞에 배치한다.
#알파벳 사전 순으로 앞에 있는 단어일수록 앞에 배치한다
import sys
n,m = map(int,sys.stdin.readline().split())
word_dict = {}
for _ in range(n):
    a = sys.stdin.readline().rstrip()
    if len(a)>=m:
        if a not in word_dict.keys():
            word_dict[a]=1
        else:
            word_dict[a]+=1
dict_keys = list(word_dict.keys())
dict_values = list(word_dict.values())
set_dict_count = list(set(dict_values))
set_dict_count.sort(reverse=True)
# set count로 for 문 
# 같은 count 가진 리스트 뽑기
# 단어의 길이 비교 sort
# 단어의 길이마저 같으면 사전순

for i in set_dict_count:
    same_list = [dict_keys[j] for j in range(len(dict_values)) if dict_values[j]==i]
    len_list = [len(k) for k in same_list]
    set_len_list = list(set(len_list))
    set_len_list.sort(reverse=True)
    for l in set_len_list:
        total_list = [same_list[temp] for temp in range(len(len_list)) if len_list[temp] == l]
        total_list.sort()
        print(*total_list,sep="\n")
