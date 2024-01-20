def fibonacci(n):
    fibo_li = []
    count = 0
    for i in range(n):
        if i==0 or i==1:
            fibo_li.append(1)
        else:
            count+=1
            fibo_li.append(fibo_li[i-2]+fibo_li[i-1])
    return fibo_li[n-1], count
num = int(input())
a, b = fibonacci(num)
print(a,b)