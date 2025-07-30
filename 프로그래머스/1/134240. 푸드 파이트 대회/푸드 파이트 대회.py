def solution(food):
    water=food[0]
    left = ""
    for i in range(1, len(food)):
        left += str(i) * (food[i] // 2)
        answer = left + "0" + left[::-1]


            
    return answer