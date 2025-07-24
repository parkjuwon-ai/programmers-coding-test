def solution(s):
    st= s.split(' ')
    j = 0 
    for i in st:
        k=int(i)
        st[j] = k 
        j += 1
        
    a= max(st)
    b= min(st)
    
    answer = str(b) + ' ' + str(a)
    return answer