def solution(n, times):
    answer=0
    start=1

    end=n*max(times)
    
    answer = binary_search(start, end, n, times)
    
    return answer

# start : 최소 시간
# end : 최대 시간
# mid : 현재 주어진 시간
# sum : mid 시간동안 입국 심사를 받을 수 있는 인원 수 
def binary_search(start, end, n, times):
    while start<end:
        #print("\nstart ",start, "end", end)
        sum=0 #인원 수
        mid=(start+end)//2
        
        for time in times:
            #print(sum, time)
            sum +=mid//time
            
        print("sum",sum)
        if sum>=n: #모든 사람이 입국 심사를 받을 수 있는 경우 -> 시간을 더 줄일 수 있는지 확인하기 위해 시간 배열의 앞에서 검사
            end=mid
        else: # 모든 사람이 받지 못한 경우 -> 시간이 부족한 것이므로 시간 배열의 뒤에서 검사
            start=mid+1
            
    return start
