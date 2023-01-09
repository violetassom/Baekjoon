def self_number():
    not_self_numbers = []
    for i in range(1,10000):
        if i < 10:
            # 1 - 9
            # 2+2
            not_self_numbers.append(i+i)
        elif i < 100:
            # 10 - 99
            # 10 + 1 + 0
            not_self_numbers.append(i+i//10+i%10)
        elif i < 1000:
            # 100 - 999
            # 100 + 1 + 0 + 0
            # 123 + 1 + 2 + 3
            not_self_numbers.append(i+i//100+(i%100)//10+i%10)
        else:
            # 1000 - 9999
            # 1234 + 1 + 2 + 3 + 4
            not_self_numbers.append(i+i//1000+(i%1000)//100+(i%100)//10+i%10)
    for j in range(1,10001):
        if j not in not_self_numbers:
            print(j)
self_number()