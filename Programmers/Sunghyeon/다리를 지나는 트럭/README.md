```py
def solution(bridge_length, weight, truck_weights):
    que=[];
    time=0;
    tmp=0;
    while(len(truck_weights)!=0):
        if(sum(que)+truck_weights[0]<=weight):
            que.append(truck_weights.pop(0));
            time=time+1;
            tmp=tmp+1;
            if(tmp==bridge_length):
                que.pop(0);
                tmp=0;
        else:
            que.pop(0);
            time=time+bridge_length;
    return time;
```

위 코드로 풀었을 때 Case 1만 통과하였습니다.

## 규칙

- 차가 다리에서 주행을 시작할 때 1초가 흐른다.
- 다리를 빠져나가는데에는 bridge_length 만큼의 시간이 소요된다.
- 다리 위 차의 수는 bridge_length 이하여야 한다.
- 다리 위 차의 무게는 weight 이하여야 한다.

## 아이디어

- 최소 다리길이 만큼의 시간이 소요된다.
-

## 케이스

1. 큐의 길이 < bridge_length
   1. 큐의 총합 + truck_weights[0] <=weight
      큐에 원소를 하나 집어넣고 time+1;
   2. 큐의 총합 + truck_weight[0] > weight
      큐에 0을 집어넣는다.
      <!-- 1-2의 경우 원소가 큐에서 나올 떄 까지 큐에 새로운 원소의 유입이 없다. -->
2. 큐의 길이 == bridge_length

   1. 큐에서 원소를 하나 제거한다.

3. len(truck_weights) ==0이되면 time+bridge_length를 해준다.
