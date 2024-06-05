# 첫번째 해시로 풀 때
# def solution(nums):
#     nums_dict = {}
#     for i in nums:
#         if i not in nums_dict.keys():
#             nums_dict[i]=1
#         else:
#             nums_dict[i]+=1
#     max_phonekemon = len(nums)//2
#     nums_dict_keys = len(nums_dict.keys())
#     if max_phonekemon>=nums_dict_keys:
#         answer = nums_dict_keys
#     else:
#         answer = max_phonekemon
#     return answer
def solution(nums):
    set_num = set(nums)
    k = len(nums)/2
    answer = min(k,len(set_num))
    return answer
