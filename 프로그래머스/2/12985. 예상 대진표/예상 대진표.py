import math
def solution(n,a,b):
    answer = 0
    # 12345678910111213141516
    # 1 2 3 '4' 5 6 '7' 8
    #  1   2     3     4
    #    1          2
    #         1
    
    # n을 절반했을 때 a랑 b가 따른 곳에 있다면 답은 무조건 log2N값임.
    # 만약 같은 곳에 있다면
    # N의 기준을 절반으로 접고 또 비교한다. a랑 b도 그에 맞게 값을 수정
    # 따른 곳에 있을 때까지 절반으로 또 비교
    # log2N값이 답임
    
    while True:
        point = int(n//2)
        if (a<=point and b>point) or (a>point and b<=point):
            return math.log2(n)
            break
        elif a<=point and b<=point:
            n = point
        else:
            a = a-point
            b = b-point
            n = point
            