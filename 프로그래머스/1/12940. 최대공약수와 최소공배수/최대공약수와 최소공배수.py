def solution(n, m):
    #최대 공약수를 구하는 법
    #n과 m의 약수 중 가장 큰 수
    x=[]
    answer = []
    for i in range(1, min(m,n)+1):
        if m%i==0 and n%i==0:
            x.append(i)
            a= x[-1]

    #최소 공배수 구하는 법
    #n과 m의 약수를 구하고 전부 곱한다   
    answer = [a, (n * m) // a]
    return answer