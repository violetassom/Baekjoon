import sys
n = int(sys.stdin.readline().rstrip())
test_case = []
for _ in range(n):
    a = int(sys.stdin.readline().rstrip())
    test_case.append(a)
max_case = max(test_case)
dp_list = []
for i in range(max_case+1):
    if i <= 3:
        dp_list.append(1)
    else:
        dp_list.append(dp_list[i-2]+dp_list[i-3])
for j in test_case:
    print(dp_list[j])