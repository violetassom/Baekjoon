count = int(input())
li = list(map(int, input().split()))
# li = [int(i) for i in input().split()]
result = 0
# breakpoint()
for i in li:
    prime = 1
    div = 3
    if i == 1:
        pass
    elif i == 2:
        result+=1
    elif i == 3:
        result+=1
    elif i % 2 != 0:
        while True:
            if i == div:
                break
            elif i % div == 0:
                prime = 0
                break
            else:
                div += 1
        if prime != 0:
            result += 1
    
print(result)