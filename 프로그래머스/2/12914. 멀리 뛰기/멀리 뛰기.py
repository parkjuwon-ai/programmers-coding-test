def solution(n):
    a= 1
    b= 2
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        for i in range(3, n+1):
            a,b= b,(a+b) % 1234567
    return b
            
    
  
