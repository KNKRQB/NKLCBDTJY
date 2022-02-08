def solution(N, number):
    answer = -1 #기본 값을 -1로 설정
    arr = [] #만든 숫자 조합 저장 배열

    for i in range(1, 9):
        numbers = set() #중복 방지를 위해 set 선언
        numbers.add( int(str(N) * i) ) #N을 붙이기만 해서 만든 숫자 set에 추가
        
        for j in range(0, i-1):
            for x in arr[j]: #맨 앞부터
                for y in arr[-j-1]: #맨 뒤부터
                    numbers.add(x + y)
                    numbers.add(x - y)
                    numbers.add(x * y)
                    
                    if y != 0: #나누기 예외처리
                        numbers.add(x // y)

        if number in numbers: #만약 만든 배열 중 숫자가 존재하면 return
            answer = i
            break
        
        arr.append(numbers)

    return answer
