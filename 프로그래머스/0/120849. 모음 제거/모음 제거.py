def solution(my_string):
    answer =""
    del_list=["a","e","i","o","u"]
    for i in my_string:
        if i not in del_list:
            answer += i
                
    return answer