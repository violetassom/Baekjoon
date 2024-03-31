#첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.

#둘째 줄에는 중앙값을 출력한다.

#셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.

#넷째 줄에는 범위를 출력한다.
def mean(x):
    return round(sum(x)/len(x))
def mid(x):
    x.sort()
    return x[int(len(x)//2)]
def mode(x):
    x.sort()
    temp = {}
    for i in x:
        if i not in temp.keys():
            temp[i]=0
        else:
            temp[i]+=1
    temp_key = list(temp.keys())
    temp_val = list(temp.values())
    max_num = max(temp_val)
    temp_list = [temp_key[j] for j in range(len(temp_val)) if temp_val[j]==max_num]
    if len(temp_list)==1:
        return temp_list[0]
    else:
        return temp_list[1]
    
def xrange(x):
    return max(x)-min(x)
import sys
n = int(sys.stdin.readline())
num_list = []
for _ in range(n):
    a = int(sys.stdin.readline())
    num_list.append(a)

print(mean(num_list))
print(mid(num_list))
print(mode(num_list))
print(xrange(num_list))