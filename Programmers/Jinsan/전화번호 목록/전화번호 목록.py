# -*- coding: utf-8 -*-

def solution(phone_book):
    answer = True
    
    phone_dict = {}#번호 담을 딕셔너리
    
    for i in phone_book:
        phone_dict[i] = 1
                
    for i in phone_dict:#딕셔너리에서 번호 하나씩 꺼내기
        tmp = ""#빈 문자
        for j in i:#꺼낸 번호에서 한 글자씩 빈 문자열에 담기
            tmp += j
            #문자열(비교할 번호)이 딕셔너리에 존재하고
            #처음에 꺼낸 번호가 아닐 경우 다른 번호의 접두어로 판단
            if tmp in phone_dict and tmp != i:
                answer = False
                return answer
    
    return True