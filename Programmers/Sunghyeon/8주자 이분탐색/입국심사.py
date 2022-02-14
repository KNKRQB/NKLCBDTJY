def solution(n, times):
    answer = 0;
    left,right=1,max(times)*n; # left는 최소시간 right는 최대시간
    while(left<=right):
        mid=(left+right)//2;
        people=0;
        for time in times:
            people += mid //time; # mid 시간동안 심사한 사람의 수
            
            if people>=n:
                break;
        
        # 검사할 수 있는 사람이 검사할 사람보다 많을 경우
        
        if people >= n:
            answer =mid;
            right = mid - 1;
            
        # 검사할 수 있는 사람이 검사할 사람보다 적을 경우
        
        elif people<n:
            left = mid + 1;
            
    return answer;