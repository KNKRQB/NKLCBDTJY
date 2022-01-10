import heapq
def solution(jobs):
    answer = 0 # 작업하는데 걸린 총 시간
    now = 0 #현재 시간(시점)
    i = 0 #처리된 작업의 개수
    start = -1 # 이전에 완료한 작업의 시작 시간
    heap = [] #현재 처리 가능한 jobs을 담는 힙
    
    while i < len(jobs):
        # 현재 시점에서 처리할 수 있는 작업을 heap에 저장
        for j in jobs:
            if start < j[0] <= now: # 이전에 끝낸 작업보다 큰 시간이고, 현재 시점보다 작은 시간인 경우 작업 가능
                heapq.heappush(heap, [j[1], j[0]]) # (처리 시간, 요청 시간)
        
        if len(heap) > 0: # 힙에 처리할 작업이 남은 경우
            current = heapq.heappop(heap) #cur은 현재 처리중인 작업
            start = now
            now += current[0]
            answer += (now - current[1]) # 작업 요청시간부터 처리 완료까지의 시간 계산
            i += 1
        else: # 처리할 작업이 없는 경우
            now += 1
            
    answer = answer // len(jobs) # 평균 처리 시간 계산
    
    return answer
