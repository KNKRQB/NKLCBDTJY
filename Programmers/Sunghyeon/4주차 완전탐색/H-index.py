def solution(citations):
    citations.sort();
    length=len(citations);
    for i in range(length):
        if(citations[i]>=length-i):
            return length-i;
    return 0

# 이상의 값이므로 길이의 최대값부터 인용횟수의 최소값부터 탐색하며 조건을 만족하는 값을 찾는다.