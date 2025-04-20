def solution(absolutes, signs):
    #result=[]
    #for i in range(len(absolutes)):
    #    if signs[i] == 0:
    #        result.append(-absolutes[i])
    #    else:
    #        result.append(absolutes[i])
    #answer = sum(result)
    return sum([-absolutes[i] if signs[i] ==0 else absolutes[i]
                for i in range(len(absolutes)) 
                ])