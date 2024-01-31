x,y,w,h=map(int,input().split())

a=x-w if x>=w else w-x
b=y-h if y>=h else h-y
li = [a,b,x,y]
li.sort()
print(li[0])