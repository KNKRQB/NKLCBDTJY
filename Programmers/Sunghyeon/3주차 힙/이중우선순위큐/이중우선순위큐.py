from collections import deque;

def solution(operations):
    deq=deque();
    for i in operations:
        # 문자열을 메소드와 숫자로 나눔
        i=i.split(' ');
        method=i[0];
        num=int(i[1]);
        
        # 삽입일 경우 덱에 넣어줌
        if(method=='I'):
            deq.append(num);
        
        # 삭제일 경우
        elif(method=='D'):
            # 삭제할 원소가 없을 경우 continue
            if(len(deq)==0):
                continue;
            
            # D 1일경우 최대값을 삭제함
            elif(num==1):
                deq.remove(max(deq));
            # D -1일 경우 최소값을 삭제함
            elif(num==-1):
                deq.remove(min(deq));
    # deq에 하나 이상의 원소가 있을 경우
    if(len(deq)):
        return [max(deq),min(deq)];
    # 아닐경우 0 0을 반환
    return [0,0];

# https://juun42.tistory.com/41 파이썬 문자열
# https://leonkong.cc/posts/python-deque.html deque
# https://wikidocs.net/77 파이썬 모듈(참고)
# https://codechacha.com/ko/python-convert-string-to-integer/ 파이썬 숫자로 변환