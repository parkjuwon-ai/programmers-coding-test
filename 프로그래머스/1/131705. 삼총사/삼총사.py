from itertools import combinations

def solution(number):
    answer = 0
    list_three=list(combinations(number,3))
    for i in list_three:
        if sum(i) == 0:
            answer += 1
        
    return answer