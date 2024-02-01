a1,b1 = map(int,input().split()) 
a2,b2 = map(int,input().split())
a3,b3 = map(int,input().split())

x = [a1,a2,a3]
y = [b1,b2,b3]

x_unique = list(set(x))
y_unique = list(set(y))

result_x = 0
result_y = 0
if x.count(x_unique[0])>x.count(x_unique[1]):
    result_x = x_unique[1]
else:
    result_x = x_unique[0]
if y.count(y_unique[0])>y.count(y_unique[1]):
    result_y = y_unique[1]
else:
    result_y = y_unique[0]
print(result_x,result_y)