def solution(cititations):
    print(cititations.sort(reverse=True))
    top = max(cititations)
    loop = len(cititations)
    for i in range(top):
        upper = 0
        lower = 0
        for j in range(cititations):
            if j >= i:
                upper+=1
            if j <= i:
                lower+=1
        if (upper >= i) and (lower <= i):
            return i
    return 0

print(solution([3,0,6,6,6,6,6,6,1,5]))