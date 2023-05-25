n = int(input())

def isPalindrome(s):
    i=0
    def recursion(s,l,r,i):
        if s[l]!=s[r]:
            i+=1
            return 0,i
        elif l>=r:
            i+=1
            return 1,i
        else:
            i+=1
            return recursion(s,l+1,r-1,i)

    return recursion(s,0,len(s)-1,i)

for _ in range(n):
    string = input()
    a,b = isPalindrome(string)
    print(a,b)