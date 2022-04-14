def solution(n, costs):
    lands = [(-1) * i - 1 for i in range(n)]
    costs.sort(key=lambda x: x[2])
    sum = 0
    for st,ed,cost in dcosts:
        if lands[st] == lands[e]:
            continue
        sum += cost
        if (lands[st] >= 0) and (lands[ed] >= 0):
            temp = lands[ed]
            for j in lands:
                if j == temp:
                    lands[lands.index(j)] = lands[st]
            continue

        if (lands[st] < 0) and (lands[ed] < 0):
            lands[st] = st
            lands[ed] = st

        if lands[st] >= 0:
            lands[ed] = lands[st]
            continue

        lands[st] = lands[ed]
    return sum


print(solution(5, [[0, 1, 5], [1, 2, 3], [2, 3, 3], [3, 1, 2], [3, 0, 4], [2, 4, 6], [4, 0, 7]]))
print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))
print(solution(5, [[0, 1, 1], [3, 4, 1], [1, 2, 2], [2, 3, 4]]))
print(solution(5, [[0, 1, 1], [2, 3, 1], [3, 4, 2], [1, 2, 2], [0, 4, 100]]))