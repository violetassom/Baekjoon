import sys
n = int(input())
def algorithm(number):
    # 기존에 있던 점 4개
    # Y=f(x)^2 
    # F(x+1)=2f(x)-1
    # F(2)=3
    if number == 1:
        return 3  
    else:
        return (algorithm(number-1)*2)-1
def algorithm2(number):
    # 기존에 있던 점 4개
    # Y=f(x)^2 
    # F(x+1)=2f(x)-1
    # F(2)=3
    return algorithm(number)**2

print(algorithm2(n))