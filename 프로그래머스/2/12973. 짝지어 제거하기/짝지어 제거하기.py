def solution(s):
    list_s= []
    for i in s:
        if list_s and list_s[-1] == i:
            list_s.pop()
        else:
            list_s.append(i)
        
        
    if len(list_s) == 0:
        answer = 1
    else:
        answer = 0

    return answer