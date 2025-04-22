def solution(d, budget):
    count = 0
    for cost in sorted(d):
        if cost <= budget:
            budget -= cost
            count += 1
        else:
            break
    return count
