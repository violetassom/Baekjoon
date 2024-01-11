### n==9일때 말이야
n=int(input())
k = [3**1, 3**2, 3**3, 3**4, 3**5, 3**6, 3**7, 3**8]
real_n = k.index(n)+1
def star(num):
    if num==1:
        return '***\n* *\n***'
    else:
        string=''
        strlist = star(num-1).split('\n')
        for i in range(3):
            for k,j in enumerate(strlist):
                if i == 1:
                    string += j + 3**(num-1)*' ' + j +'\n'
                elif i == 0 :
                    string += j*3 + '\n'
                else:
                    if k==len(strlist)-1:
                        string += j*3
                    else:
                        string += j*3 + '\n'
        return string

print(star(real_n))