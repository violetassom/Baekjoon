import sys
n = int(sys.stdin.readline())
contact_list = ['ChongChong']

for _ in range(n):
    a,b = sys.stdin.readline().rstrip().split()
    if a in contact_list:
        if b not in contact_list:
            contact_list.append(b)
    elif b in contact_list:
        if a not in contact_list:
            contact_list.append(a)
print(len(contact_list))