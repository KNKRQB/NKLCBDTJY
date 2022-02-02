import heapq


def solution(money):
    house = [[i, money[i]] for i in range(len(money))]
    total = sum(money)
    house.sort(key=lambda x: x[1], reverse=True)

    asw = 0
    for hos, mon in house:
        if total == 0:
            break
        if money[hos] == 0:
            continue
        asw += mon
        total -= mon
        total += money[hos]
        total += money[hos+1]
        total += money[hos-1]


        money[hos] = 0
        money[hos+1] = 0
        money[hos-1] = 0

    return asw

def solution1(money):
    house = []
    #heapq.heapify(money)
    for item in range(len(money)):
        heapq.heappush(house, [-(money[item]), money[item], item])

    heapq.
    return house

def solution2(money):
    dp1 = [0] * len(money)
    dp2 = [0] * len(money)
    # 1번 집을 터는 경우
    dp1[0] = money[0]
    for i in range(1, len(money) - 1): # 마지막 집은 털지 못함
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + money[i])
    # 1번 집을 안터는 경우
    dp2[0] = 0
    for i in range(1, len(money)):
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + money[i])
    return max(dp1[-2], dp2[-1])
    #출처: https: // mjmjmj98.tistory.com / 109[Live passionate😎]




print(solution1([1,2,3,1]))