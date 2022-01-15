def solution(prices):
    answer = []
    for i in range(0,len(prices)):
        answer.append(0);
        for j in range(i+1,len(prices)):
            answer[i]=answer[i]+1
            if(prices[i]>prices[j]):        
               break; 
    return answer

print(solution([1, 2, 3, 2, 3]))