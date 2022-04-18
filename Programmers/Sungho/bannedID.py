def solution(user_id, banned_id):
    ans = []
    sig = True
    bcount = 0
    ucount = 0
    for bid in banned_id:
        bcount += 1
        print(bcount)
        temp = set()
        for uid in user_id:
            ucount += 1
            print(bcount, ucount, temp, ans)
            if len(bid) == len(uid):
                for i in range(len(bid)):
                    if (bid[i] != '*') and (bid[i] != uid[i]):
                        sig = False
                        break
                if sig:
                    temp.add(uid)
                sig = True
        ans.append(temp)
    print(ans)
    total = 1
    for item in ans:


    return total
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))