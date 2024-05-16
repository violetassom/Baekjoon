def solution(arr1, arr2):
    
    r1,c1 = len(arr1), len(arr1[0])
    r2,c2 = len(arr2), len(arr2[0])
    # len(arr1)*len(arr1[0]) * len(arr2)*len(arr2[0])
    # 최종 결과물은 len(arr1) * len(arr2[0])
    
    # [[1, 4],  [[3, 3],
    # [3, 2],    [3, 3]]
    # [4, 1]]	
    
    # arr1[0][0]*arr2[0][0] + arr1[0][1]*arr2[1][0], arr1[0][1]*arr2[1][0] + arr1[0][1]*arr2[1][1]
    # arr1[i][i]*arr2[j][j] + arr1[i][i+1]*arr2[j+1][j],
    # arr1[i][i+1]*arr2[j+1][j] + arr1[i][i+1]*arr2[j+1][j+1]
    
    
    """
    232 543
    424 241    
    314 311
    """
    # arr1[0][0]*arr2[0][0] + arr1[0][1]*arr2[1][0] + arr1[0][2]*arr2[2][0]
    answer = [[0]*len(arr2[0]) for _ in range(len(arr1))]
    # arr1[0][0]*arr2[0][0] + arr1[0][1]*arr2[1][0]
    # arr1[0][1]*arr2[1][0] + arr1[0][1]*arr2[1][1]
    # 0 1 2
    for i in range(len(arr1)):
        # 0 1 2
        for j in range(len(arr2[0])):
            for k in range(len(arr2)):
                answer[i][j]+=arr1[i][k]*arr2[k][j]
            
    
    return answer