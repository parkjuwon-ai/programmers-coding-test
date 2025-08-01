def solution(s):
    
    count_transforms = 0  
    count_zeros = 0       

    
    while s != "1":
        
        num_zeros = s.count("0")
        count_zeros += num_zeros

        
        s = s.replace("0", "")

        
        length = len(s)
        s = bin(length)[2:]  

        
        count_transforms += 1

    return [count_transforms, count_zeros]
