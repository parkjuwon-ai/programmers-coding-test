def solution(s):
    if s[0] == '+':
        num=s.replace('+', '') 
        answer = int(num)
    else:
        answer = int(s)
    
    return answer