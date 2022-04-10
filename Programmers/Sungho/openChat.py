def solution(record):
    #0  Enter uid name
    #1  Leave uid
    #2  Change uid name


    users = [[-1],[-1]]
    priOut = [[-1],[-1]]
    for rec in record:
        order = rec.split()[0]
        uid = rec.split()[1]

        if(order == "Enter"):
            if uid in users[0]:    #입장 전적이 있음
                users[1][users[0].index(uid)] = rec.split()[2]

            else:   #입장 전적 없음
                users[0].append(uid)
                users[1].append(rec.split()[2])
            priOut[0].append(uid)
            priOut[1].append(0)

        elif(order == "Leave"):
            priOut[0].append(uid)
            priOut[1].append(1)
        else:
            users[1][users[0].index(uid)] = rec.split()[2]
    ans = []
    temp = dict()
    #uid: name
    for uid, order in zip(priOut[0],priOut[1]):
        if order == -1:
            continue
        print(temp, ans)
        if uid in temp:
            name = temp[uid]
        else:
            name = users[1][users[0].index(uid)]
            temp[uid] = name

        if order == 0:
            tt = name + "님이 들어왔습니다."
        elif order == 1:
            tt = name + "님이 나갔습니다."
        else:
            continue
        ans.append(tt)
    print(tt)
    return ans

solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])