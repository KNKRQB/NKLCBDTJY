# -*- coding: utf-8 -*-

def solution(prices):
    answer = []
    
    prices_len = len(prices)
    
    for i in range(prices_len):
        answer.append(0)
        for j in range(i+1,prices_len):
            if prices[i] <= prices[j]: #다음 가격이 더 크거나 같을 경우
                answer[i] += 1
            else: #다음 가격이 더 작을 경우
                answer[i] += 1
                break
    
    return answer