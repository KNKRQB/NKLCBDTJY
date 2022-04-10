def solution(m, musicinfos):

    note = []
    lion = []
    for nt in m:
        if nt != '#':
            lion.append(ord(nt))
        else:
            lion[-1] += 100

    list = []
    for i in musicinfos:
        #str end name mel
        temp = i.split(',')
        str = temp[0]
        end = temp[1]
        name = temp[2]
        mel = temp[3]
        print(str, end, name, mel)
        str = int(str[0:2]) * 60 + int(str[3:5])
        end = int(end[0:2]) * 60 + int(end[3:5])
        song = []
        print(str, end)
        for nt in mel:
            if nt != '#':
                song.append(ord(nt))
            else:
                song[-1] += 100
        print(song)
        playTime = end - str
        if playTime < len(song):
        #too short
            note.append(song[0:playTime])
        else:
        #too long
            note.append(song * int(playTime/len(song)) + song[0:playTime%len(song)])

        if 66 in song:
            print("hello")
        list.append(song)

    print(note)
    #for i in note:
        #note = [[66,65,165,70], ...]

    return 1
print(int(5/3))
str = ['A','B','C','D','E', 'D', 'F','G']
solution("CC#BCC#BCC#BCC#B",["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"])
