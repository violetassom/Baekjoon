import sys
while True:
    a,b,c = map(int,input().split())
    if a==0 and b==0 and c==0:
        break
    else:
        li = [a,b,c]
        li.sort()
        # print(li)
        # print(li[0]+li[1]<=li[2])
        if a==b and b==c:
            print("Equilateral")
        elif li[0]+li[1]<=li[2]:
            print("Invalid")    
        elif a==b or a==c or b==c:
            print("Isosceles")
        else:
            print("Scalene")