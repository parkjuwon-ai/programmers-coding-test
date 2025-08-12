def solution(n):
    a, b= 1, 1
    if n==2:
        return 1
    elif n==3:
        return 2
    
    else:
        for i in range(3,n+1):
            a, b= b,(a+b)%1234567
    
    return b