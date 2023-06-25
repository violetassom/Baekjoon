li = []
max_len = 0
for _ in range(5):
    temp_li = []
    input_s = list(input())
    li.append(input_s)
    if max_len < len(input_s):
        max_len = len(input_s)
for j in range(max_len):
    for i in range(5):
        try:
            print(li[i][j],end='')
        except:
            pass