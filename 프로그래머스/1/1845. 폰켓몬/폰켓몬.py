def solution(nums):
    nums_dict = {}
    for i in nums:
        if i not in nums_dict.keys():
            nums_dict[i]=1
        else:
            nums_dict[i]+=1
    max_phonekemon = len(nums)//2
    nums_dict_keys = len(nums_dict.keys())
    if max_phonekemon>=nums_dict_keys:
        answer = nums_dict_keys
    else:
        answer = max_phonekemon
    return answer