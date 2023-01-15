# 그룹으로 나눠야한다.
# 같은 알파벳들은 떨어져있으면 안된다.
#
counts = int(input())
result = 0
for i in range(counts):
    emp_dict = dict()
    word = list(input())
    for j in word:
        if j not in emp_dict.keys():
            emp_dict[j] = 1
        else:
            var = emp_dict[j]
            emp_dict[j] = var + 1
    ex = ''
    for k, l in emp_dict.items():
        ex = ex + str(k) * int(l)
    if ex == ''.join(word):
        result += 1
    else:
        pass

print(result)