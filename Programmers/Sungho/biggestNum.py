def solution(numbers):
    for i in range(len(numbers)):
        numbers[i] = str(numbers[i])
    numbers.sort(key = lambda x: x[0], reverse=True)

    answer = ''
    for j, k in enumerate(numbers):

        answer += j

    return answer

print(solution([3,30,34,5,9]))