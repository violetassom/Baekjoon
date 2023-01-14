word = input()
croatia_alp = ['c=','c-','dz=','d-','lj','nj','s=','z=']
for i in croatia_alp:
    if i in word:
        word = word.replace(i,'1')
print(len(word))