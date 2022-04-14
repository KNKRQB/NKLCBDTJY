def solution(numbers, hand):
    #       0    1   2   3
    #0      1    4   7   *
    #1      2    5   8   0
    #2      3    6   9   #

    keys = [[1,4,7,-1], [2,5,8,0], [3,6,9,-2]]

    #   x   y
    l = [0, 3]
    r = [2, 3]

    ans = ""
    for num in numbers:
        if num in keys[0]:
            ans += 'L'
            l[0] = 0
            l[1] = keys[0].index(num)
        elif num in keys[2]:
            ans += 'R'
            r[0] = 2
            r[1] = keys[2].index(num)
        else:
            loc = keys[1].index(num)
            llen = abs(l[0] - 1) + abs(l[1] - loc)
            rlen = abs(r[0] - 1) + abs(r[1] - loc)
            if llen < rlen:
                l[0] = 1
                l[1] = loc
                ans += 'L'
            elif rlen < llen:
                r[0] = 1
                r[1] = loc
                ans += 'R'
            else:
                if hand == "left":
                    l[0] = 1
                    l[1] = loc
                    ans += 'L'
                elif hand == "right":
                    r[0] = 1
                    r[1] = loc
                    ans += 'R'

        print(l, r, num, ans)
    return ans
print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
#l -> [0,1]     r -> [2,0]   tg -> [1,1]
