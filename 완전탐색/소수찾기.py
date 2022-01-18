import itertools

#소수 판별 함수
def is_prime_number(x):
    if x < 2: #0과 1은 소수가 아님
        return False
    
    # 2부터 (x - 1)까지의 모든 수를 확인하며
    for i in range(2, x):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임

def solution(numbers):
    answer = 0
    combi = []
    str=""
    for j in range(1, len(numbers)+1): #모든 문자열 조합 찾기
        for i in itertools.permutations(numbers, j):
            combi.append(int("".join(list(i))))
            
    #리스트에서 중복 문자열 제거
    myset = set(combi)
    mylist = list(myset) 
    #print(mylist)
    
    for num in mylist:
        print(num)
        print(is_prime_number(num))
        if is_prime_number(num)==True:
            answer += 1
    
    return answer