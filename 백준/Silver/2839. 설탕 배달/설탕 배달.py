
kilogram = int(input())
li = []
three = 0
if kilogram%5 ==0 :
    li.append(kilogram//5)
if kilogram%3 ==0 :
    li.append(kilogram//3)
while True:
    three+=1
    if three >= kilogram//3:
        break
    else:
        if (kilogram-3*three)%5 == 0:
            li.append((kilogram-3*three)//5+three)

if len(li) != 0:
    print(min(li))
else:
    print(-1)