def solution(n):
    if n % 2 == 1:
        answer = '수'+'박수'*(n//2)
    else:
        answer = '수박'*(n//2)
    return answer