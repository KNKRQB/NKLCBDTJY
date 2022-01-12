def solution(operations):
    que = []

    for i in operations:
        if i == "D 1":
            try:
                que.remove(max(que))
            except:
                print("D1 err")
        elif i == "D -1":
            try:
                que.remove(min(que))
            except:
                print("D-1 err")
        else:
            temp = i.split()
            que.append(int(temp[1]))

    if len(que) == 0:
        que = [0,0]
    else:
        que = [max(que), min(que)]
    return que
