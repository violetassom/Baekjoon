def solution(prices):
    # for i in prices
    #   for j in range(i,len(prices))
    # if i >= j break 
    # 개수세기
    answer = []
    for i in range(len(prices)):
        a=0
        for j in range(i+1,len(prices)):
            # print(i,j)
            if prices[i]<=prices[j]:
                a+=1
            else:
                a+=1
                break
        answer.append(a)
    return answer