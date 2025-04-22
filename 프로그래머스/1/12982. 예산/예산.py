def solution(d, budget):

    total_cost = 0
    answer = 0

    for x in sorted(d, reverse=False):
        if total_cost + x <= budget:
            total_cost += x
            answer += 1

    return answer
