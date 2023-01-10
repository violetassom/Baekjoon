def ishansu(x):
    # 123
    num1 = x//100
    num2 = (x//10)%10
    num3 = x%10
    if (num1 - num2) == (num2 - num3):
        return 1
    else:
        return 0
        
def hansus():
    result_list = []
    for i in range(1,1001):
      if i < 10:
        result_list.append(i)
      elif i < 100:
        result_list.append(i)
      elif i < 1000:
        if ishansu(i)==1:
            result_list.append(i)
      else:
        pass
    return result_list

def hansu(x):
    hl = hansus()
    result_list = [i for i in hl if i<=x]
    result = len(result_list)
    return result

input_x = int(input())
print(hansu(input_x))