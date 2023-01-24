li = list()
for i in range(5):
    num = int(input())
    li.append(num)
li.sort()
avg = sum(li)/len(li)
med = li[2]
print(int(avg))
print(int(med))