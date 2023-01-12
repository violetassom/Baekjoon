word = input()
upper_word = word.upper()
upper_word_list = list(upper_word)
set_word_list = list(set(upper_word_list))
emp_list = []
for i in set_word_list:
    emp_list.append(upper_word_list.count(i))
max_count = max(emp_list)
if emp_list.count(max_count) >= 2:
    print('?')
else:
    print(set_word_list[emp_list.index(max_count)])
