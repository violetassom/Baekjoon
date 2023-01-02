import sys
origin_num = int(sys.stdin.readline())
num1 = origin_num
i=0
while True:
    i+=1
    num1_1 = num1//10
    num1_2 = num1%10
    add_num = (num1_1 + num1_2)%10
    num1 =num1_2*10 + add_num
    if origin_num == num1:
        print(i)
        break
# 26 8
# 68 14 -> 4
# 84 12 -> 2
# 42 6
# 26
