a1 = int(input())
a2 = int(input())
# a1, a2 = map(int, input().split())
# a1, a2 = input(), input()
# 472 385
# breakpoint()
a3 = a1 * (a2 % 10)
a4 = a1 * ((a2 // 10) % 10)
a5 = a1 * (a2//100)

a6 = a3 + (a4*10) + (a5*100)

print(a3)
print(a4)
print(a5)
print(a6)