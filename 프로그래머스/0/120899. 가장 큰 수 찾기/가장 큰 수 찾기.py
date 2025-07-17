def solution(array):
    answer = []
    a= array[:] 
    array.sort()
    b= array[-1]
    answer.append(b)
    answer.append(a.index(b))

    return answer