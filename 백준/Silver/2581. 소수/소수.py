
m = int(input())
n = int(input())


def is_prime_number(num):
    if num == 1:
        return False
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True


def output_func(m, n):
    sosu_list = []
    for i in range(m, n + 1):
        if is_prime_number(i):
            sosu_list.append(i)
    sosu_list.sort()
    if len(sosu_list) == 0:
        print('-1')
    else:
        print(sum(sosu_list))
        print(sosu_list[0])


output_func(m, n)
