def solution(n):
    answers=[]
    for i in range (1, n+1):
        if n % i == 0:
            answers.append((i, n//i))
    answer = len(answers)
    return answer