n = int(input())
for i in range(n):
    h,w,customer = map(int,input().split())
    if h!=1:
        number = customer//h + 1
        floor = customer%h
        if floor == 0:
            floor = h
            number = customer // h
        else:
            pass
    else:
        number = customer
        floor = 1

    if number >= 10:
        print(f'{floor}{number}')
    else:
        print(f'{floor}0{number}')

# 2 3 4
# 4//2 + 1 = 3
# 4%2 = 0ㄷ