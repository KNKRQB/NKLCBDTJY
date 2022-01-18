import heapq
def solution(operations):
    answer = []
    hp = []
    for i in operations:
        
        if i[0] == "I":
            heapq.heappush(hp, int(i[2:]))
        else:
            if len(hp) == 0:
                pass
            elif i[2]== "-":
                heapq.heappop(hp)
            else:
                hp = heapq.nlargest(len(hp), hp)[1:]
                heapq.heapify(hp)
                
    if hp:
        answer.append(max(hp))
        answer.append(min(hp))    
    else:
        answer.append(0)
        answer.append(0)
        
    return answer
