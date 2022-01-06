def solution(operations):
    que = []

    for i in operations:
        print(que)
        if i == "D 1":
            try:
                print("max: ", max(que))
                que.remove(max(que))
            except:
                print("D1 err")
        elif i == "D -1":
            try:
                print("min: ", min(que))
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

print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))
list = [-45, -642]
print(max(list), min(list))