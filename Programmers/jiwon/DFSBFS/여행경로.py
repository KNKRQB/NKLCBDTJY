list = [] #가능한 여행경로를 모두 저장

def solution(tickets):
    answer = []
    visited = [False]*len(tickets) #티켓 개수만큼 방문 여부 생성
    index = 0
    
    dfs(index, "ICN", "ICN", tickets, visited)
    
    list.sort() #알파벳 순서대로 정렬
    #print(list)
    answer = list[0].split(" ") 

    return answer

def dfs(index, start, result, tickets, visited):
    #print(index, result)
    if index == len(tickets): #모든 여행지를 방문한 경우
        list.append(result) #여행 경로 저장
        return
    
    for i in range(len(tickets)):
        if visited[i]==False and tickets[i][0] == start:
            visited[i] = True
            dfs(index+1, tickets[i][1], result+" "+tickets[i][1], tickets, visited)
            visited[i]=False
