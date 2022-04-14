# -*- coding: utf-8 -*-

def solution(numbers):
    answer = ''
    
    l = []
    
    for i in numbers: #숫자를 문자열로 변경
        l.append(str(i))
    
    #문제 요구 조건에 맞게 정렬
    #정렬 기준 key 값이 x*3인 이유는 numbers의 원소가 0~1000이기에
    #최소 세자릿수를 맞춰주기 위함, 그래야 올바른 비교 가능
    l.sort(key = lambda x: x*3, reverse = True)
    
    
    
    for i in l:
        answer += i
    
    #print(answer)

    #[0,0]의 경우 00이 나오기에 int로 변경 후 다시 str로
    return str(int(answer))