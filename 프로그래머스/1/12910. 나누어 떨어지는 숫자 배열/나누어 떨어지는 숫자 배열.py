def solution(arr, divisor):
    #array리스트를 순회하면서 divisor로 나누어 떨어지는 값을 구함
    answer = []
    for i in arr:
        if i % divisor == 0:
            #answer에 값을 추가    
            answer.append(i)
    #배열에 -1 반환
    if len(answer) == 0:
        answer.append(-1)
    #오름차순 정렬
    else:
        answer.sort()
    return answer