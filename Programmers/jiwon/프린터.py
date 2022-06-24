from collections import deque

def solution(priorities, location):
    answer = 0
    d = deque([(v,i) for i,v in enumerate(priorities)]) #(우선순위, 인덱스)를 쌍으로 만들어서 큐에 저장
    
    while d:
        item = d.popleft() #큐의 맨 앞 원소 꺼내기 -> item[0]은 우선순위, item[1]은 문서의 인덱스
        if d and max(d)[0] > item[0]: #현재 꺼낸 원소가 우선순위가 가장 크지 않은 경우
            d.append(item) #인쇄하지 않고 큐의 뒤에 다시 넣기
        else: #현재 꺼낸 원소가 우선순위가 가장 높은 경우
            answer += 1 #현재 문서 인쇄
            if item[1] == location: #만약 원하는 문서의 인덱스가 현재 원소랑 같은 경우
                break #반복문 탈출
    
    return answer
