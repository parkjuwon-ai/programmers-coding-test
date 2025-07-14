def solution(price, money, count):
    pay = 0
    for i in range(count+1):
        pay += price*i
    result= pay - money 
    if result > 0:
        answer = result
    else:
        answer = 0

    return answer