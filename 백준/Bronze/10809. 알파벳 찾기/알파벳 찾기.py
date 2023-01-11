# 97 122
string = input()
#abcdefghijklmnopqrstuvwxyz
for i in range(97,123):
    if chr(i) in string:
        print(string.index(chr(i)),end=" ")
    else:
        print("-1",end=" ")
        