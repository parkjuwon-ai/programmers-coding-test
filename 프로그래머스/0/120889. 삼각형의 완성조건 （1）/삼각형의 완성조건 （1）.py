def solution(sides):
    a = max(sides)
    sides.remove(a)
    if a < sum(sides):
        answer = 1
    else:
        answer = 2
    return answer