def solution(n, costs):
    answer = 0
    costs.sort(key = lambda x :(x[2]))
    
    node = set([costs[0][0], costs[0][1]])
    answer = costs[0][2]
    
    while len(node) < n:
        for cost in costs :
            if cost[0] in node and cost[1] in node:
                continue
            if cost[0] in node or cost[1] in node:
                node.update([cost[0], cost[1]])
                answer += cost[2]
                break
                
    return answer