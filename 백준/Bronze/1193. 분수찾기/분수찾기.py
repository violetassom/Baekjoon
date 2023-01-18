# 1/1 1/2 1/3 1/4
# 2/1 2/2 2/3 2/4
# 3/1 3/2 3/3 3/4

#1 1/1

#2 1/2
#3 2/1

#4 3/1
#5 2/2
#6 1/3

#7 1/4
#8 2/3
#9 3/2
#10 4/1

#11 5/1
#12 4/2
#13 3/3
#14 2/4
#15 1/5

number = int(input())
an = 1
total_an = 1
while True:
    if number <= total_an:
        break
    else:
        an += 1
        total_an += an
# 몇번쨰의 수인가?
count_number = total_an - number + 1
# breakpoint()
# 12345
# 54321
if an%2 == 0:
    numer = an - count_number + 1
    denom = count_number
    print(f'{numer}/{denom}')
else:
    numer = count_number
    denom = an - count_number + 1
    print(f'{numer}/{denom}')
# fountain_number(number)