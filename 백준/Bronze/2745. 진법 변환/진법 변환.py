import sys
n,b = sys.stdin.readline().split()
n_list = list(n)
b = int(b)
def chr_to_int(numlist):
    result = []
    for i in numlist:
        if i.isdigit():
            result.append(int(i))
        else:
            result.append(ord(i)-55)
    return result
number_list = chr_to_int(n_list)
def b_formation_ten(N,B):
    result = 0
    for i,j in enumerate(N):
        result += B**(len(N)-i-1)*j
    return result
print(b_formation_ten(number_list,b))