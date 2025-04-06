def solution(s):
    lenth=len(s)
    if lenth % 2 == 1:
        return s[lenth//2]
    else:
        return s[lenth//2-1:lenth//2+1]