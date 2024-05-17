def solution(s):
    answer = True
    my_stack = []
    
    # for i in s:
    #     if i=='(':
    #         my_stack.append(i)
    #     else:
    #         if not my_stack:
    #             return False
    #         else:
    #             my_stack.pop()
    # if my_stack:
    #     answer=False
    
    for i in s:
        if i=='(':
            my_stack.append(i)
        else:
            if not my_stack:
                return False
            else:
                if my_stack[-1]=='(':
                    my_stack.pop()
                else:
                    my_stack.append(i)
            
    
    # for idx,val in enumerate(s):
    #     if idx == 0:
    #         if val == ")":
    #             return False
    #         else:
    #             my_stack.append('(')
    #     else:
    #         if val == "(":
    #             my_stack.append('(')
    #         else:
    #             if my_stack[-1]=='(':
    #                 my_stack.pop()
    #             else:
    #                 my_stack.append(')')
    if my_stack:
        answer = False
                
                
    return answer