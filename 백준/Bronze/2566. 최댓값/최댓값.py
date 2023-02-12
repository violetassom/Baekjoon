input_list = list()
for i in range(9):
    m1 = list(map(int,input().split()))
    input_list.append(m1)
# breakpoint()
max_li = max(map(max,input_list))
print(max_li)

for j in range(len(input_list)):
    if max_li in input_list[j]:
        print(j+1,end=' ')
        print(input_list[j].index(max_li)+ 1)
        break