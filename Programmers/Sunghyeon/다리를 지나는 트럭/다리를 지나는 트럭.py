def solution(bridge_length, weight, truck_weights):
    que=[];
    time=0;
    while(len(truck_weights)!=0):
        print(que,truck_weights,time);
        if(len(truck_weights)==0):
            return time;
        if(len(que)<bridge_length):
            if(sum(que)+truck_weights[-1]<=weight):
                que.append(truck_weights.pop(0));
                time=time+1;
            elif(sum(que)+truck_weights[-1]>weight):
                que.append(0);
                time=time+1;
        else:
            que.pop(0);
    time=time+bridge_length;
    return time;

print(solution(	100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))

# 큐의 길이 < bridge_length
    # 큐의 총합 + 다음 원소 <= weight
        # 큐에 원소를 하나 집어넣고 time+1;
    # 아닐 경우(>)
        # 0을 집어넣는다.
        
# 큐의 길이 == bridge_length
    # 큐에서 하나 뺀다

# https://gomguard.tistory.com/138 파이썬 배열 전체 합
# https://ooeunz.tistory.com/7 파이썬 스택
# https://www.daleseo.com/python-queue/ 파이썬 큐