# 손익분기점 총 수입(판매비용) >= 총 비용(=고정비용+가변비용)
# c(판매가격) * x(총 개수) >= (a+b) * x(총 개수)
a,b,c = map(int,input().split())
if c-b <= 0:
    print('-1')
else:
    print(a//(c-b)+1)