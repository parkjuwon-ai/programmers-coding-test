def solution(n):
    three=''
    while n > 0:
        three = str(n % 3) + three
        n = n//3
        
    j=1
    ten=0
    for i in three:
        ten += int(i) * j
        j=j*3
        
    answer = ten
    return answer