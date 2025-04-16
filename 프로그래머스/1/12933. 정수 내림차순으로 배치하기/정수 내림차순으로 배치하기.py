def solution(n):
    s=str(n)
    l=list(s)
    l.sort(reverse=True)
    answer=''.join(l)
    return int(answer)