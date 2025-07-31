def solution(name, yearning, photo):
    name_year = []
    answer = []
    name_year = dict(zip(name, yearning))
           
    for p in photo:
        score=0
        for i in p:
            if i in name_year:
                score += name_year[i]
        answer.append(score)    
    
    return answer