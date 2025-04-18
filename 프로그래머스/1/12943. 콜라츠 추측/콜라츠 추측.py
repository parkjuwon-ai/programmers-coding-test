def solution(num):
    if num == 1:
        answer = 0
    else:
        answer =0
        while num != 1:
            if num % 2 == 1:
                num = num * 3 +1
                answer += 1
            else: 
                num = num // 2
                answer += 1
        
        if answer >= 500:
            answer = -1
                
    return answer            
            
            
            
            
            
            
            
            
            
            
            
            
        
        
        
        
        
        
        
    answer = 0
    return answer