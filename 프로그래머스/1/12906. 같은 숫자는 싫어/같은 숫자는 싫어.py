def solution(arr):
    answer = [arr[0]]
    for i in arr:
        if i != answer[-1]:
            answer.append(i)
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')
    return answer