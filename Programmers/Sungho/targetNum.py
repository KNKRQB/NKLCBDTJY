def solution(numbers, target):

    #nums = [[item, -item] for item in numbers ]
    ans = []
    ans.append([0])
    for i in numbers:
        temp = []
        for j in ans[-1]:
            temp.append(j + i)
            temp.append(j - i)
        ans.append(temp)
    return ans[-1].count(target)

print(solution([1, 1, 1, 1, 1], 3))
