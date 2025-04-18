def solution(a, b):
    if a == b:
        answer = a
    elif a > b:
        r = abs(b - a) + 1
        answer=(a + b)/2*r
    else: 
        r = abs(a - b) + 1
        answer=(a + b)/2*r
    return answer