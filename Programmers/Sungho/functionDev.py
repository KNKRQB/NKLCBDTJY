import math

def solution(progresses, speeds):
    answer = []
    period = []
    for i in range(len(progresses)):
        period.append(math.ceil((100 - progresses[i]) / speeds[i]))

    idx = 0
    count = 0
    std = period[idx]
    while idx < len(progresses):
        print(std, period[idx], count)
        if std >= period[idx]:
            count += 1
        else:
            answer.append(count)
            count = 0
            std = period[idx]
            continue

        idx += 1

    answer.append(count)
    return answer

progresses = [93, 30, 55]
speeds = [1, 30, 5]

print(solution(progresses, speeds))
