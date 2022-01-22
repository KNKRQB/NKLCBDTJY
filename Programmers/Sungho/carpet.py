def solution(brown, yellow):
    rowcol = (brown - 4) / 2

    #yellow 의 곱 짝 찾기
    for i in range(1, yellow + 1):
        if (yellow % i == 0) and ((yellow / i + i)  == rowcol):
            answer = [int(yellow / i + 2), i + 2]
            answer.sort(reverse=True)
            return answer

    return 0