# 쿼터(Quarter, $0.25)의 개수, 다임(Dime, $0.10)의 개수, 니켈(Nickel, $0.05)의 개수, 페니(Penny, $0.01)
import sys
n = int(sys.stdin.readline())

def change(num):
    change_li = []
    change_li.append(num//25)
    num2 = num%25
    change_li.append(num2//10)
    num3 = num2%10
    change_li.append(num3//5)
    num4 = num3%5
    change_li.append(num4//1)
    return change_li

for _ in range(n):
    amount = int(sys.stdin.readline())
    result_li = change(amount)
    print(*result_li)