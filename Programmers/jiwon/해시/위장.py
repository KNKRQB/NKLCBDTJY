def solution(clothes):
    answer = 1
    dic = {} #dictionary 사용
    
    for i in range(len(clothes)):
        kind = clothes[i][1]
        if kind in dic:
            dic[kind] += 1
        else:
            dic[kind] = 1
            
    for k in dic.keys():
        print(k)
        answer *= (dic[k]+1)
    answer -= 1
    return answer