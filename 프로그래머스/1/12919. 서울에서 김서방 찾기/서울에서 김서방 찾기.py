def solution(seoul):
    where=0
    for i in seoul:
        if i == 'Kim':
            answer = f'김서방은 {where}에 있다'
        else:
            where += 1
    return answer