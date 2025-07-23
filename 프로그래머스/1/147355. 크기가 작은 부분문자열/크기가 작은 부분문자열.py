def solution(t, p):
    p_len=len(p)
    t_len=len(t)
    answers=[]
    # t의 길이로 나눈 p의 길이
    for i in range (t_len-p_len+1):
        if int(p) >= int(t[i: p_len+i]):
            answers.append(int(t[i: t_len+i]))
    
    answer = len(answers)
    return answer