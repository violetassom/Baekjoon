import sys
nums = int(sys.stdin.readline().rstrip())

for i in range(nums):
#    result=(nums-i)*' ' + str((i+1)*'*')
#    print(result)
    print((nums-(i+1))*' '+(i+1)*'*')