import sys
a = input()
def ispalindrome(string):
    b = len(string)//2
    result = 1
    for i in range(b):
        if string[i]==string[len(string)-i-1]:
            pass
        else:
            result = 0
            break
    return result
print(ispalindrome(a))