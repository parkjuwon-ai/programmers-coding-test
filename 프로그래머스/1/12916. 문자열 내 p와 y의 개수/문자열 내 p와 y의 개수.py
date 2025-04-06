def solution(s):
    text=s.upper()
    p_count=text.count('P')
    y_count=text.count('Y')
    if p_count == y_count:
        answer = True
    
    else:
        answer = False
    

    
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return answer