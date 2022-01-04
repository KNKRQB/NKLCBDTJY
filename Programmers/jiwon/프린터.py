from collections import deque

def solution(priorities, location):
    answer = 0
    d = deque([(v,i) for i,v in enumerate(priorities)]) #(우선순위, 인덱스)
    
    while d:
        item = d.popleft()
        if d and max(d)[0] > item[0]: #중요도가 가장 높지 않은 문서
            d.append(item)
        else:
            answer += 1 #현재 문서 인쇄
            if item[1] == location:
                break
    
    return answer