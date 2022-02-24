def solution(n, results):
    answer = 0
    win = {}
    lose = {}
    
    for i in range(1, n+1):
        win[i] = set() # 중복 방지를 위해 set 사용
        lose[i] = set()
        
    for result in results:
        win[result[0]].add(result[1]) # 해당 인덱스 선수에게 진 선수 저장
        lose[result[1]].add(result[0]) # 해당 인덱스 선수를 이긴 선수 저장
        
    for i in range(1,n+1):
        for winner in lose[i]:
            win[winner].update(win[i])
        for loser in win[i]:
            lose[loser].update(lose[i])
            
    for i in range(1,n+1):
        if len(win[i]) + len(lose[i]) == n-1 :
            answer += 1
            
    return answer
