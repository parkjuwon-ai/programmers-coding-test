def solution(n):
    #n의 약수 구하기
    #어떻게? 약수는 n이 1과 자기 자신 
    #몫이 1이 나올때 까지 반복문을 돌리자
    #무엇으로 나누지?
    #n보다 작은수로 
    answer = 0
    for i in range(1, n+1):
        if n % i == 0:
            answer += i
        else:
            pass
    #n을 모두 더하기    
    
    return answer

